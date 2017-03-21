from django import template 
from datetime import *
from django.template.defaultfilters import stringfilter
from itertools import *
from h2_1.utilities.moon.moon import fm_series, flmoons_since

register = template.Library()



@register.simple_tag
@register.filter
@stringfilter
def nights():
    today = date.today()
    future = date(2058,2,16)
    nights = (future-today).days
    # nights = '{:.{prec}f}'.format(nights, prec=0)
    nights = '{:,}'.format(nights)

    return nights



@register.simple_tag
@register.filter
@stringfilter
def today():
    return date.today()


@register.simple_tag
@register.filter
@stringfilter
def days():
    today = date.today()
    mn_list_str_1 = str(today.year) + '/' + str(today.month) + '/' + str(today.day)
    mn_list_str_2 = str(today.year + 1) + '/' + str(today.month) + '/' + str(today.day)
    future = date(2058,2,16)
    days = (future - today).days
    return days

@register.simple_tag
@register.filter
@stringfilter
def weeks():
    today = date.today()
    mn_list_str_1 = str(today.year) + '/' + str(today.month) + '/' + str(today.day)
    mn_list_str_2 = str(today.year + 1) + '/' + str(today.month) + '/' + str(today.day)
    future = date(2058,2,16)
    days = (future - today).days
    weeks = round(((future-today).days/7),1)
    weeks = '{:,}'.format(weeks)
    return weeks 

@register.simple_tag
@register.filter
@stringfilter
def months():
    today = date.today()
    mn_list_str_1 = str(today.year) + '/' + str(today.month) + '/' + str(today.day)
    mn_list_str_2 = str(today.year + 1) + '/' + str(today.month) + '/' + str(today.day)
    future = date(2058,2,16)
    days = (future - today).days
    months = round(((future-today).days/30.44),1)
    months = '{:,}'.format(months)
    return months 

@register.simple_tag
@register.filter
@stringfilter
def lunar_months():
    today = date.today()
    mn_list_str_1 = str(today.year) + '/' + str(today.month) + '/' + str(today.day)
    mn_list_str_2 = str(today.year + 1) + '/' + str(today.month) + '/' + str(today.day)
    future = date(2058,2,16)
    days = (future - today).days
    lunar_months = round(((future-today).days/29.53),1)
    return lunar_months

@register.simple_tag
@register.filter
@stringfilter
def years():
    today = date.today()
    mn_list_str_1 = str(today.year) + '/' + str(today.month) + '/' + str(today.day)
    mn_list_str_2 = str(today.year + 1) + '/' + str(today.month) + '/' + str(today.day)
    future = date(2058,2,16)
    days = (future - today).days    
    years = round(((future-today).days/365.25),1)
    return years

@register.simple_tag
@register.filter
@stringfilter
def mars_years():
    today = date.today()
    mn_list_str_1 = str(today.year) + '/' + str(today.month) + '/' + str(today.day)
    mn_list_str_2 = str(today.year + 1) + '/' + str(today.month) + '/' + str(today.day)
    future = date(2058,2,16)
    days = (future - today).days    
    mars_years = round(((future-today).days/668.5991),1)
    return mars_years 

@register.simple_tag
@register.filter
@stringfilter
def moon_list():
    today = date.today()
    mn_list_str_1 = str(today.year) + '/' + str(today.month) + '/' + str(today.day)
    mn_list_str_2 = str(today.year + 1) + '/' + str(today.month) + '/' + str(today.day) 
    moon_list = fm_series( mn_list_str_1, mn_list_str_2)
    return moon_list 

@register.simple_tag
@register.filter
@stringfilter
def fm_since_uc_married():
    today = date.today()
    mn_list_str_2 = str(today.year + 1) + '/' + str(today.month) + '/' + str(today.day)    
    uc_married_dt = '1987/9/18'
    offcly_married_dt = '1988/8/27'
    fm_since_uc_married = flmoons_since(uc_married_dt, mn_list_str_2)[0]
    return fm_since_uc_married 

@register.simple_tag
@register.filter
@stringfilter
def fm_since_of_married():
    today = date.today()
    mn_list_str_2 = str(today.year + 1) + '/' + str(today.month) + '/' + str(today.day)    
    uc_married_dt = '1987/9/18'
    offcly_married_dt = '1988/8/27'
    fm_since_of_married = flmoons_since(offcly_married_dt, mn_list_str_2)[0]
    return fm_since_of_married 

@register.simple_tag
@register.filter
@stringfilter
def bm_since_of_married():
    today = date.today()
    mn_list_str_2 = str(today.year + 1) + '/' + str(today.month) + '/' + str(today.day)    
    uc_married_dt = '1987/9/18'
    offcly_married_dt = '1988/8/27'
    bm_since_of_married = flmoons_since(offcly_married_dt, mn_list_str_2)[1]
    return bm_since_of_married 


nights.is_safe = True
today.is_safe = True
days.is_safe = True
months.is_safe = True
lunar_months.is_safe = True
years.is_safe = True
mars_years.is_safe = True
moon_list.is_safe = True
fm_since_uc_married.is_safe = True
fm_since_of_married.is_safe = True
bm_since_of_married.is_safe = True


# @register.tag(name="evaluate")
# def do_evaluate(parser, token):
#     """
#     tag usage {% evaluate object.textfield %}
#     """
#     try:
#         tag_name, variable = token.split_contents()
#         print(variable)
#     except ValueError:
#         raise template.TemplateSyntaxError("{0!r} tag requires a single argument".format(token.contents.split()[0]))
#     return EvaluateNode(variable)

# class EvaluateNode(template.Node):
#     def __init__(self, variable):
#         self.variable = template.Variable(variable)

#     def render(self, context):
#         try:
#             content = self.variable.resolve(context)

#             t = template.Template(content)
#             return t.render(context)
#         except template.VariableDoesNotExist or template.TemplateSyntaxError("Template syntax error."):
#             return 'Error rendering', self.variable


    # today = date.today()
    # mn_list_str_1 = str(today.year) + '/' + str(today.month) + '/' + str(today.day)
    # mn_list_str_2 = str(today.year + 1) + '/' + str(today.month) + '/' + str(today.day)
    # future = date(2058,2,16)
    # days = (future - today).days
    # # days = '{:.{prec}f}'.format(days, prec=1)
    # days = '{:,}'.format(days)
    # weeks = round(((future-today).days/7),1)
    # # weeks = '{:.{prec}f}'.format(weeks, prec=1)
    # weeks = '{:,}'.format(weeks)
    # months = round(((future-today).days/30.44),1)
    # # months = '{:.{prec}f}'.format(months, prec=1)
    # months = '{:,}'.format(months)
    # lunar_months = round(((future-today).days/29.53),1)
    # years = round(((future-today).days/365.25),1)
    # #years = '{:.{prec}f}'.format(years, prec=1)
    # mars_years = round(((future-today).days/668.5991),1)
    # # mars_years = '{:.{prec}f}'.format(mars_years, prec=1)
    # moon_list = fm_series( mn_list_str_1, mn_list_str_2)
    # uc_married_dt = '1987/9/18'
    # offcly_married_dt = '1988/8/27'
    # fm_since_uc_married = flmoons_since(uc_married_dt, mn_list_str_2)[0]
    # fm_since_of_married = flmoons_since(offcly_married_dt, mn_list_str_2)[0]
    # bm_since_of_married = flmoons_since(offcly_married_dt, mn_list_str_2)[1]



    #     'date': date,
    #     "days": days,
    #     "weeks": weeks,
    #     "months": months,
    #     "lunar_months": lunar_months,
    #     "years": years,
    #     "mars_years": mars_years,
    #     "moon_list": moon_list,
    #     "fm_since_uc_married": fm_since_uc_married,
    #     "fm_since_of_married": fm_since_of_married,
    #     "bm_since_of_married": bm_since_of_married,
     