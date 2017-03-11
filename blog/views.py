from urllib import parse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, redirect, render 
from django.template import Context, loader, RequestContext
from django.db.models import Q

from blog.models import Post 
from blog.forms import PostForm


##########################
# Helper functions       #
##########################


def get_popular_posts():
    popular_posts = Post.objects.filter(status='p').order_by('-views')[:5]
    return popular_posts



def prepare_posts_by_category(request, category, cat):
    '''
    Takes category and category abbreviation(cat), collects filtered list (by category, status=published, order, limit), and 
    returns template_name and context_dict in a tuple for view functions template rendering.
    '''
    latest_posts = Post.objects.all().filter(category=cat).filter(status='p').order_by('-created_date')[:10]
    
    date = ''
    for post in latest_posts:
        date = post.created_date.strftime('%a, %d %b %Y')
    paginator = Paginator(latest_posts, 3)

    queryset_list = Post.objects.all().filter(status='p')
    query = request.GET.get("q")

    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(tag__icontains=query)
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
    template_name = 'index.html'
    context_dict = {
        'latest_posts': queryset,
        'popular_posts': get_popular_posts(),
        'date': date,
        'category': category,
        'page_request_var': page_request_var,
        'query': query,
    }

    return (template_name, context_dict)   




##########################
# View functions         #
##########################

def healthspan(request):
    prepared_posts = prepare_posts_by_category(request, 'Healthspan', 'hs')
    return render(request, prepared_posts[0], prepared_posts[1])

def training(request):
    prepared_posts = prepare_posts_by_category(request, 'Training', 'tr')
    return render(request, prepared_posts[0], prepared_posts[1])

def eating(request):
    prepared_posts = prepare_posts_by_category(request, 'Eating', 'et')
    return render(request, prepared_posts[0], prepared_posts[1])

def sleeping(request):
    prepared_posts = prepare_posts_by_category(request, 'Sleeping', 'sl')
    return render(request, prepared_posts[0], prepared_posts[1])

def learning(request):
    prepared_posts = prepare_posts_by_category(request, 'Learning', 'ln')
    return render(request, prepared_posts[0], prepared_posts[1])

def other(request):
    prepared_posts = prepare_posts_by_category(request, 'Other', 'ot')
    return render(request, prepared_posts[0], prepared_posts[1])


def post(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    instance.views +=1
    instance.save()
    if instance.image:
        print(instance.image.url)
    date = instance.created_date.strftime('%a, %d %b %Y')

    
    query = request.GET.get("q")
    if query:
        queryset_list = Post.objects.all().filter(status='p')
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(tag__icontains=query)
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
        template_name = 'index.html'
        context_dict = {
            'latest_posts': queryset,
            'popular_posts': get_popular_posts(),
            'date': date,
            'category': category,
            'page_request_var': page_request_var,
            'query': query,
        }
        return render(request, template_name, context_dict)


    else:
        context_dict = {
            'instance': instance,
            'popular_posts': get_popular_posts(),
            'date': date,
        }
    return render(request, 'blog/post.html', context_dict)










#############################
#   REFERENCE Functions     #
#############################

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    share_string = parse.quote(instance.preview)
    context = {
        "title": instance.title,
        "instance": instance,
        "popular_posts":get_popular_posts(),
        "share_string": share_string,
    }
    return render(request, "blog/post_detail.html", context)


def add_post(request):    
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_authenticated:
        raise Http404
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=True)
            instance.user = request.user 
            instance.save()
            messages.success(request, "<a href='#'>Item1</a> Saved", extra_tags='html_safe')
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            print(form.errors)
    else:
        # request.method is GET
        form = PostForm()

        # context = RequestContext(request)
    context = { 
        "form": form,
    }
    return render(request, 'blog/add_post.html', context)





def update_post(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_authenticated:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    slug = instance.slug
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> saved", extra_tags='html_safe')

        return HttpResponseRedirect(instance.get_absolute_url())
        # return redirect('post', category=instance.category)

    context = {
        "title": instance.title,
        "instance": instance,
        "form":form,
        "slug": instance.slug
    }
    return render(request, "blog/add_post.html", context)


def delete_post(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_authenticated:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)

    if instance.category == 'hs':
        instance.delete()
        message = messages.success(request, "Successfully deleted")
        return redirect('blog:healthspan')
    elif instance.category == 'tr':
        instance.delete()
        message = messages.success(request, "Successfully deleted")
        return redirect('blog:training') 
    elif instance.category == 'et':
        instance.delete()
        message = messages.success(request, "Successfully deleted")
        return redirect('blog:eating') 
    elif instance.category == 'sl':
        instance.delete()
        message = messages.success(request, "Successfully deleted")
        return redirect('blog:sleeping') 
    elif instance.category == 'ln':
        instance.delete()
        message = messages.success(request, "Successfully deleted")
        return redirect('blog:learning') 
    elif instance.category == 'ot':
        instance.delete()
        message = messages.success(request, "Successfully deleted")
        return redirect('blog:other') 


###############
# Variations  #
###############
# def post(request, slug=None):

#     instance = get_object_or_404(Post, slug=slug)
#     instance.views += 1
#     instance.save()
#     if instance.image:
#         print(instance.image.url)

#     date = instance.created_date.strftime('%a, %d %b %Y')
    
#     t = loader.get_template('blog/post.html')
#     context_dict = {
#         'instance': instance,
#         'popular_posts': get_popular_posts(),
#         'date': date,
#     }
#     c = Context(context_dict)
#     return HttpResponse(t.render(c))

# class URLRedirectView(View):
#     def get(self, request, slug=slug, *args, **kwargs):
#         obj = get_object_or_404(Post, slug=slug) 
#         # Save analytic data item
#         print(ClickEvent.objects.create_event(obj))
#         return HttpResponseRedirect(obj.url)