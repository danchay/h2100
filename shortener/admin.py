from django.contrib import admin

from .models import ShURL

class ShURLAdmin(admin.ModelAdmin):
	list_display = ('url', 'active')


admin.site.register(ShURL, ShURLAdmin)