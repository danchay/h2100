from django.contrib import admin
from blog.models import Post 

from django.db import models
from pagedown.widgets import AdminPagedownWidget



class PostAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

    class Meta:
        model = Post
        app_label = 'Blog Posts'
    
    list_display = ['id','category', 'tag', 'title', 'slug','status', 'created_date', 'updated' ]
    list_display_links = ['title']
    ordering = ['category', 'status', 'updated', 'created_date'  ]
    list_editable = ['tag']
    list_filter = [ 'category', 'status', 'created_date', 'updated']
    search_fields = ['title', 'tag', 'body_text', 'header_text']
    actions = ['make_published', 'make_draft', 'make_withdrawn', 'cat_healthspan', 'cat_training', 'cat_eating', 'cat_sleeping', 'cat_learning', 'cat_other']
    prepopulated_fields = {"slug": ("title",)}

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

    def make_withdrawn(self, request, queryset):
        rows_updated = queryset.update(status='w')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfuly marked as withdrawn." % message_bit)
    make_withdrawn.short_description = "Mark selected stories as withdrawn"

    def cat_healthspan(self, request, queryset):
        rows_updated = queryset.update(category='hs')
        if rows_updated == 1:
            message_bit = "One story was"
        else:
            message_bit = "%s stories were" % rows_updated 
        self.message_user(request, "%s successfully categorized in 'healthspan'" % message_bit)
    cat_healthspan.short_description = "Categorize selected stories as 'healthspan'"

    def cat_training(self, request, queryset):
        rows_updated = queryset.update(category='tr')
        if rows_updated == 1:
            message_bit = "One story was"
        else:
            message_bit = "%s stories were" % rows_updated 
        self.message_user(request, "%s successfully categorized in 'training'" % message_bit)
    cat_training.short_description = "Categorize selected stories as 'training'"

    def cat_eating(self, request, queryset):
        rows_updated = queryset.update(category='et')
        if rows_updated == 1:
            message_bit = "One story was"
        else:
            message_bit = "%s stories were" % rows_updated 
        self.message_user(request, "%s successfully categorized in 'eating'" % message_bit)
    cat_eating.short_description = "Categorize selected stories as 'eating'"

    def cat_sleeping(self, request, queryset):
        rows_updated = queryset.update(category='sl')
        if rows_updated == 1:
            message_bit = "One story was"
        else:
            message_bit = "%s stories were" % rows_updated 
        self.message_user(request, "%s successfully categorized in 'sleeping'" % message_bit)
    cat_sleeping.short_description = "Categorize selected stories as 'sleeping'"

    def cat_learning(self, request, queryset):
        rows_updated = queryset.update(category='ln')
        if rows_updated == 1:
            message_bit = "One story was"
        else:
            message_bit = "%s stories were" % rows_updated 
        self.message_user(request, "%s successfully categorized in 'learning'" % message_bit)
    cat_learning.short_description = "Categorize selected stories as 'learning'"

    def cat_other(self, request, queryset):
        rows_updated = queryset.update(category='ot')
        if rows_updated == 1:
            message_bit = "One story was"
        else:
            message_bit = "%s stories were" % rows_updated 
        self.message_user(request, "%s successfully categorized in 'other'" % message_bit)
    cat_other.short_description = "Categorize selected stories as 'other'"



admin.site.register(Post, PostAdmin)
