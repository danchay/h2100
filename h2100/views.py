from datetime import *
from .utilities.moon.moon import fm_series, flmoons_since

from urllib import parse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, redirect, render 
from django.template import Context, loader, RequestContext
from django.db.models import Q

from blog.models import Post 



def about(request):
    today = date.today()
    mn_list_str_1 = str(today.year) + '/' + str(today.month) + '/' + str(today.day)
    mn_list_str_2 = str(today.year + 1) + '/' + str(today.month) + '/' + str(today.day)
    future = date(2058,2,16)
    days = (future - today).days
    # days = '{:.{prec}f}'.format(days, prec=1)
    days = '{:,}'.format(days)
    weeks = round(((future-today).days/7),1)
    # weeks = '{:.{prec}f}'.format(weeks, prec=1)
    weeks = '{:,}'.format(weeks)
    months = round(((future-today).days/30.44),1)
    # months = '{:.{prec}f}'.format(months, prec=1)
    months = '{:,}'.format(months)
    lunar_months = round(((future-today).days/29.53),1)
    years = round(((future-today).days/365.25),1)
    #years = '{:.{prec}f}'.format(years, prec=1)
    mars_years = round(((future-today).days/668.5991),1)
    # mars_years = '{:.{prec}f}'.format(mars_years, prec=1)
    moon_list = fm_series( mn_list_str_1, mn_list_str_2)
    uc_married_dt = '1987/9/18'
    offcly_married_dt = '1988/8/27'
    fm_since_uc_married = flmoons_since(uc_married_dt, mn_list_str_2)[0]
    fm_since_of_married = flmoons_since(offcly_married_dt, mn_list_str_2)[0]
    bm_since_of_married = flmoons_since(offcly_married_dt, mn_list_str_2)[1]


    context = {
        "days": days,
        "weeks": weeks,
        "months": months,
        "lunar_months": lunar_months,
        "years": years,
        "mars_years": mars_years,
        "moon_list": moon_list,
        "fm_since_uc_married": fm_since_uc_married,
        "fm_since_of_married": fm_since_of_married,
        "bm_since_of_married": bm_since_of_married,
        }
    return render(request, "about.html", context )

def get_popular_posts():
    popular_posts = Post.objects.order_by('-views')[:5]
    return popular_posts

def index(request):
    
    latest_posts = Post.objects.all().filter(status='p').order_by('-created_date')[:10]

    date = ''
    for post in latest_posts:
        date = post.created_date.strftime('%a, %d %b %Y')
    paginator = Paginator(latest_posts, 8)
    category = "Hacking to 100"


    queryset_list = Post.objects.all()
    query = request.GET.get("q")
    if query:
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

    t = loader.get_template('index.html')
    context_dict = {
        'latest_posts': queryset,
        'popular_posts': get_popular_posts(),
        'date': date,
        'category': category,
        'page_request_var': page_request_var,
    }
    c = Context(context_dict)
    return HttpResponse(t.render(c))