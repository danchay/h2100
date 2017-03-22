from django.contrib import admin
from blog.models import Post, Category, BlogRoll 
from django.utils.html import format_html

from django.db import models
# from pagedown.widgets import AdminPagedownWidget

class BlogRollAdmin(admin.ModelAdmin):
	class Meta:
		model = BlogRoll 
		app_label = "Blog Roll"
	list_display = ['name', 'description', 'url']
	list_display_links = ['name']
	ordering = ['name']
	list_filter = ['name']
	list_editable = ['url']
	search_fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
	class Meta:
		model = Category 
		app_label = 'Categories'

	list_display = ['id', 'title', 'slug']
	list_display_links = ['title']
	ordering = ['id']
	list_filter = ['title']
	search_fields = ['title']


class PostAdmin(admin.ModelAdmin):

    # formfield_overrides = {
    #     models.TextField: {'widget': AdminPagedownWidget },
    # }


    class Meta:
        model = Post
        app_label = 'Blog Posts'
    
    list_display = ['id',  'title', 'slug','status','display_categories', 'display_tags', 'created', 'modified' ]
    list_display_links = ['title']
    ordering = [ 'status', 'modified', 'created'  ]
    list_filter = [ 'status', 'created', 'modified']
    search_fields = ['title', 'display_tags', 'body', 'teaser']
    actions = ['make_published', 'make_draft']
    # prepopulated_fields = {"slug": ("title",)}

    def get_tags_queryset(self, request):
    	return super(PostAdmin, self).get_tags_queryset(request).prefetch_related('tags')

    def get_categories_queryset(self, request):
    	return super(PostAdmin, self).get_categories_queryset(request).prefetch_related('categories')

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='p')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfuly marked as published." % message_bit)
    make_published.short_description = "Mark selected stories as published"

    def make_draft(self, request, queryset):
        rows_updated = queryset.update(status='d')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfuly marked as draft." % message_bit)
    make_draft.short_description = "Mark selected stories as draft"


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogRoll, BlogRollAdmin)

