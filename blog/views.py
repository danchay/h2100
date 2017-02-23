from django.shortcuts import get_object_or_404, render_to_response, redirect, render 

from django.http import HttpResponse
from django.template import Context, loader, RequestContext

from blog.models import Post 
from blog.forms import PostForm


##########################
# Helper functions       #
##########################


def get_popular_posts():
    popular_posts = Post.objects.order_by('-views')[:5]
    return popular_posts



def prepare_posts_by_category(request, category, cat):
    '''
    Takes category and category abbreviation(cat), collects filtered list (by category, status=published, order, limit), and 
    returns template_name and context_dict in a tuple for view functions template rendering.
    '''
    latest_posts = Post.objects.all().filter(category=cat).filter(status='p').order_by('-created_date')[:3]
    
    date = ''
    for post in latest_posts:
        date = post.created_date.strftime('%a, %d %b %Y')

    template_name = 'blog/index.html'
    context_dict = {
        'latest_posts': latest_posts,
        'popular_posts': get_popular_posts(),
        'date': date,
        'category': category,
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





def index(request):
    latest_posts = Post.objects.all().order_by('-created_date')[:3]


    for post in latest_posts:
        date = post.created_date.strftime('%a, %d %b %Y')

    t = loader.get_template('blog/index.html')
    context_dict = {
        'latest_posts': latest_posts,
        'popular_posts': get_popular_posts(),
        'date': date,
    }
    c = Context(context_dict)
    return HttpResponse(t.render(c))


def post(request, slug):

    single_post = get_object_or_404(Post, slug=slug)
    single_post.views += 1
    single_post.save()

    date = single_post.created_date.strftime('%a, %d %b %Y')

    t = loader.get_template('blog/post.html')
    context_dict = {
        'single_post': single_post,
        'popular_posts': get_popular_posts(),
        'date': date,
    }
    c = Context(context_dict)
    return HttpResponse(t.render(c))


def add_post(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect(index)
        else:
            print(form.errors)
    else:
        # request.method is GET
        form = PostForm()
    return render_to_response('blog/add_post.html', {'form': form}, context)
    # render_to_response doesn't make the request available in the response. Not recommended. Likely to be deprecated.