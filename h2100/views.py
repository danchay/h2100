from django.shortcuts import render
from datetime import *


def about(request):
	today = date.today()
	future = date(2058,2,16)
	days = (future - today).days
	# days = '{:.{prec}f}'.format(days, prec=1)
	days = '{:,}'.format(days)
	weeks = int((future-today).days/7)
	# weeks = '{:.{prec}f}'.format(weeks, prec=1)
	weeks = '{:,}'.format(weeks)
	months = int((future-today).days/12)
	# months = '{:.{prec}f}'.format(months, prec=1)
	months = '{:,}'.format(months)
	years = int((future-today).days/365.25)
	years = '{:.{prec}f}'.format(years, prec=1)
	mars_years = int((future-today).days/668.5991)
	mars_years = '{:.{prec}f}'.format(mars_years, prec=1)


	context = {
		"days": days,
		"weeks": weeks,
		"months": months,
		"years": years,
		"mars_years": mars_years
		}
	return render(request, "about.html", context )

def healthspan(request):
	context = {}
	return render(request, "healthspan.html", context)