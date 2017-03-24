from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, redirect, render 
from django.template import Context, loader, RequestContext
from django.views.generic import DetailView, ListView
from urllib import parse

from blog.models import Post, Category, BlogRoll
from taggit.models import Tag


def get_popular_posts():
    popular_posts = Post.objects.filter(status='p').order_by('-visits')[:5]
    return popular_posts

def index(request):
    category = 'Hacking to 100'
    title =''
    pub_date = ''
    latest_posts = Post.objects.all().filter(status='p').order_by('-publish')[:10]


    for post in latest_posts:
        pub_date = post.publish.strftime('%a, %d %b %Y')
        post_id = post.id   
        title = post.title
        categories = post.display_categories()
    

        tags = post.display_tags()

    paginator = Paginator(latest_posts, 3)
    

    queryset_list = Post.objects.all().filter(status='p')
    query = request.GET.get("q")
    tags = Tag.objects.all()
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) | 
            Q(tags__slug__icontains=query)
            ).distinct()
        if len(queryset_list) > 0:
            paginator = Paginator(queryset_list, 8)
            category = "Search Results"
        else:
            paginator = Paginator(latest_posts, 8)
            category = "Hacking to 100"
            messages.info(request, 'No results for that search term.')

    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)  

    context = {
        'latest_posts': queryset,
        'title': title,
        'category': category,
        'page_request_var': page_request_var,
        'popular_posts': get_popular_posts(),
        'query': query,


    }
    return render(request, 'blog/index.html', context)

def post(request, slug=None):
    pub_date=''
    instance = get_object_or_404(Post, slug=slug)
    instance.visits +=1
    instance.save()
    if instance.image:
        print(instance.image.url)
    pub_date = instance.publish.strftime('%a, %d %b %Y')
    
    tags = instance.display_tags
    
    query = request.GET.get("q")
    if query:
        queryset_list = Post.objects.all().filter(status='p')
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(tags__slug__icontains=query)
            ).distinct()

        paginator = Paginator(queryset_list, 8)
        category = "Search Results"

    
        page_request_var = "page"
        page = request.GET.get(page_request_var)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            queryset = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            queryset = paginator.page(paginator.num_pages)    

        # template_name = 'blog/index.html'
        # template_name = 'index.html'


        context_dict = {
            'latest_posts': queryset,
            'popular_posts': get_popular_posts(),
            'pub_date': pub_date,
            'category': category,
            'page_request_var': page_request_var,
            'query': query,
            'tags': tags,
        }
        return render(request, 'blog/index.html', context_dict)


    else:
        context_dict = {
            'instance': instance,
            'popular_posts': get_popular_posts(),
            'pub_date': pub_date,
            'tags': tags,
        }
    return render(request, 'blog/post.html', context_dict)

def prepare_posts_by_category(request, category, *args, **kwargs):
    '''
    Takes category and category abbreviation(cat), collects filtered list (by category, status=published, order, limit), and 
    returns template_name and context_dict in a tuple for view functions template rendering.
    '''
    pub_date=''
    cat = Category.objects.get(title=category)

    latest_posts = Post.objects.all().filter(categories=cat).filter(status='p').order_by('-created')[:10]
    
    date = ''
    for post in latest_posts:
        pub_date = post.publish.strftime('%a, %d %b %Y')
    paginator = Paginator(latest_posts, 3)

    queryset_list = Post.objects.all().filter(status='p')
    query = request.GET.get("q")

    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(tags__slug__icontains=query)
            ).distinct()
        if len(queryset_list) > 0:
            paginator = Paginator(queryset_list, 8)
            category = "Search Results"
        else:
            paginator = Paginator(latest_posts, 8)
            category = "Hacking to 100"
            messages.info(request, 'No results for that search term.')

    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)    

    # template_name = 'blog/index.html'
    template_name = 'blog/index.html'
    context_dict = {
        'latest_posts': queryset,
        'popular_posts': get_popular_posts(),
        'pub_date': pub_date,
        'category': category,
        'page_request_var': page_request_var,
        'query': query,
    }

    return (template_name, context_dict)   




##########################
# Category Views         #
##########################

def healthspan(request):
    prepared_posts = prepare_posts_by_category(request, 'Healthspan')
    return render(request, prepared_posts[0], prepared_posts[1])

def training(request):
    prepared_posts = prepare_posts_by_category(request, 'Training')
    return render(request, prepared_posts[0], prepared_posts[1])

def eating(request):
    prepared_posts = prepare_posts_by_category(request, 'Eating')
    return render(request, prepared_posts[0], prepared_posts[1])

def sleeping(request):
    prepared_posts = prepare_posts_by_category(request, 'Sleeping')
    return render(request, prepared_posts[0], prepared_posts[1])

def learning(request):
    prepared_posts = prepare_posts_by_category(request, 'Learning')
    return render(request, prepared_posts[0], prepared_posts[1])

def other(request):
    prepared_posts = prepare_posts_by_category(request, 'Other')
    return render(request, prepared_posts[0], prepared_posts[1])


