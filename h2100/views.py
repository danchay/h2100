from datetime import *
from itertools import *
from .utilities.moon.moon import fm_series, flmoons_since
from functools import reduce
from urllib import parse

from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, redirect, render 
from django.template import Context, loader, RequestContext, Template
from urllib import parse

from blog.models import Post, Category, BlogRoll

def get_popular_posts():
    popular_posts = Post.objects.filter(status='p').order_by('-visits')[:5]
    return popular_posts





def about(request, slug=None):
    instance = get_object_or_404(Post, slug='about-this-site')
    if instance.status == 'd':
        messages.info(request, 'The about-this-site page is in draft state.')
        return redirect('index')
    instance.visits +=1
    instance.save()
    if instance.image:
        print(instance.image.url)
    # rendered = Template("{% load night_tags %}", instance.body).render(Context())

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

    
    query = request.GET.get("q")
    if query:
        queryset_list = Post.objects.all().filter(status='p')
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(tags__slug__icontains=query)
            ).distinct()

        category = "Search Results"

        context_dict = {
            'latest_posts': queryset,
            'popular_posts': get_popular_posts(),
            'date': date,
            'category': category,
            'page_request_var': page_request_var,
            'query': query,
            'tags': tags,

        }
        return render(request, 'blog/index.html', context_dict)

    context = {
        'instance': instance,
        'popular_posts': get_popular_posts(),
        'current_date': today,
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




def bad_request(request):
    response = render_to_response('400.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 400
    return response


def permission_denied(request):
    response = render_to_response('403.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 403
    return response

def page_not_found(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def server_error(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

