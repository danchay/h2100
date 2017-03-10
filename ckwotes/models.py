from django.db import models
from django.template.defaultfilters import truncatewords # or truncatechars

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published')
    )

class Ckwote(models.Model):
    ckwote = models.TextField(help_text='Exclude quotation marks.')
    essence = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True, help_text='Exclude --. Order first name, last name. Use "Unknown" or "Anonymous" or "A me ipso serva me" as appropriate.')
    circa = models.DateTimeField(blank=True, null=True)
    added_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    source = models.TextField(blank=True, null=True, help_text='Citation format.')
    theme = models.CharField(max_length=100, blank=True, null=True)
    tag = models.CharField(max_length=20, blank=True, null=True)

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='Draft')

    def __str__(self):
        return str('"' + self.ckwote + '"' + ' --' + self.author)

    class Meta:
        ordering=["author", "theme", "tag"]

    @property 
    def short_ckwote(self):
        return truncatewords(self.ckwote, 25)

    @property 
    def short_essence(self):
        return truncatewords(self.essence, 25)