from django.contrib import admin
from ckwotes.models import Ckwote
from django.db import models 

class CkwoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Ckwote
        app_label = 'Quote'
        verbose_name_plural = 'Quotes'

    list_display = ['id', 'short_ckwote', 'short_essence', 'author','publish_choice', 'status', 'circa', 'theme', 'tag']

    list_display_links = ['short_ckwote']
    ordering = ['theme', 'author', 'tag', 'status']
    list_editable = ['theme', 'tag']
    list_filter = ['author', 'theme', 'tag', 'status']

    search_fields = ['ckwote', 'tag', 'my_take']
    actions = ['make_published', 'make_draft', 'choose_ckwote', 'choose_m_take']


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


    def choose_ckwote(self, request, queryset):
        rows_updated = queryset.update(publish_choice='c')
        if rows_updated == 1:
            message_bit = "1 ckwote was"
        else:
            message_bit = "%s ckwotes were" % rows_updated
        self.message_user(request, "%s successfuly chosen to feature." % message_bit)
    choose_ckwote.short_description = "Feature ckwotes."

    def choose_m_take(self, request, queryset):
        rows_updated = queryset.update(publish_choice='m')
        if rows_updated == 1:
            message_bit = "1 m_take was"
        else:
            message_bit = "%s m_take were" % rows_updated
        self.message_user(request, "%s successfuly chosen to feature." % message_bit)
    choose_m_take.short_description = "Feature m_takes."

    


admin.site.register(Ckwote, CkwoteAdmin)

