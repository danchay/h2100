from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import truncatewords_html
from django.utils.safestring import mark_safe
from django.utils.timezone import now

from autoslug import AutoSlugField
from taggit.managers import TaggableManager

def upload_location(instance, filename):
    return "%s/%s % (instance.category, filename)"

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')
        ordering = ('title',)

    def __str__(self):
        return str(self.title)



class Post(models.Model):
    STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    )

    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from ='title')
    author = models.ForeignKey(User, blank=True, null=True)
    author_alias = models.CharField(max_length=100, blank=True, null=True)
    tease = models.TextField(blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to=upload_location, 
        blank=True, null=True,
        width_field="width_field",
        height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    media_url = models.URLField(blank=True, null=True)
    reference = models.TextField(blank=True)
    reference_url = models.URLField(blank=True, null=True)
    visits = models.IntegerField(default=0)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    allow_comments = models.BooleanField(default=False)
    publish = models.DateTimeField(default=now)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, blank=True)
    tags = TaggableManager(blank=True)
    meta_description = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = ('Post')
        verbose_name_plural = ('Posts')
        ordering = ('-publish',)
        get_latest_by = 'publish'

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:post", kwargs={"slug": self.slug})

    def display_categories(self):
        return ', '.join([ category.title for category in self.categories.all() ])
    display_categories.short_description = "Categories"

    def display_tags(self):
        return ', '.join([ tag.name for tag in self.tags.all() ])
    display_tags.short_description = "Tags"



class BlogRoll(models.Model):
    """Other blogs you follow."""
    name = models.CharField(max_length=100)
    url = models.URLField()
    sort_order = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=500, blank=True)
    relationship = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ('sort_order', 'name',)
        verbose_name = ('blog roll')
        verbose_name_plural = ('blog roll')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.url

