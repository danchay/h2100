from django.shortcuts import render
from datetime import *
from .utilities.moon.moon import fm_series, flmoons_since



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

def healthspan(request):
	context = {}
	return render(request, "healthspan.html", context)

