from django.contrib import admin
from ckwotes.models import Ckwote
from django.db import models 

class CkwoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Ckwote
        app_label = 'Quote'
        verbose_name_plural = 'Quotes'

    list_display = ['id', 'short_ckwote', 'short_essence', 'author', 'circa', 'theme', 'tag', 'status']
    list_display_links = ['short_ckwote']
    ordering = ['theme', 'author', 'tag', 'status']
    list_editable = ['theme', 'tag']
    list_filter = ['author', 'theme', 'tag', 'status']
    search_fields = ['ckwote', 'tag', 'essence']
    actions = ['make_published', 'make_draft']

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='p')
        if rows_updated == 1:
            message_bit = "1 quote was"
        else:
            message_bit = "%s quotes were" % rows_updated
        self.message_user(request, "%s successfuly marked as published." % message_bit)
    make_published.short_description = "Mark selected quotes as published."

    def make_draft(self, request, queryset):
        rows_updated = queryset.update(status='d')
        if rows_updated == 1:
            message_bit = "1 quote was"
        else:
            message_bit = "%s quotes were" % rows_updated
        self.message_user(request, "%s successfuly marked as draft." % message_bit)
    make_draft.short_description = "Mark selected quotes as draft."


admin.site.register(Ckwote, CkwoteAdmin)
