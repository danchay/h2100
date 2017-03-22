from django.db import models
from django.template.defaultfilters import truncatewords # or truncatechars
from blog.models import Category


STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published')
    )

PUBLISH_CHOICES = (
	('c', 'Ckwote'),
	('m', 'My Take'),
)

class Ckwote(models.Model):
    ckwote = models.TextField(help_text='Exclude quotation marks.')
    author = models.CharField(max_length=150, blank=True, null=True, help_text='Use "Unknown" or "Anonymous" or "Ex me ipso" (Out of myself) as appropriate.')
    circa = models.CharField(max_length=150, blank=True, null=True)
    source = models.TextField(blank=True, null=True, help_text='Citation format.')
    source_url = models.URLField(blank=True, null=True)
    my_take = models.TextField(blank=True, null=True)
    m_author = models.CharField(max_length=150, blank=True, null=True, help_text='Ex me ipsa')
    publish_choice = models.CharField(max_length=1, choices=PUBLISH_CHOICES, default='Ckwote')
    added_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='Draft')
    theme = models.CharField(max_length=100, blank=True, null=True)
    tag = models.CharField(max_length=20, blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)
    

    def __str__(self):
        if self.publish_choice == 'c':
            return str('"' + self.ckwote + '"' + ' --' + self.author)
        elif self.publish_choice == 'm':
            return str('"' + self.my_take + '"' + ' --' + self.m_author)

    class Meta:
        ordering=["author", "theme", "tag"]

    @property 
    def short_ckwote(self):
        return truncatewords(self.ckwote, 25)

    @property 
    def short_essence(self):
        return truncatewords(self.my_take, 25)


