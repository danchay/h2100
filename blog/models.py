from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save

from uuslug import uuslug
# from django.utils.text import slugify
from markdown_deux import markdown

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
    )

CATEGORY_CHOICES = (
    ('tr', 'Training'),
    ('hs', 'Healthspan'),
    ('et', 'Eating'),
    ('sl', 'Sleeping'),
    ('ln', 'Learning'),
    ('ot', 'Other'),
    )

def upload_location(instance, filename):
    return "%s/%s" % (instance.category, filename)

class Post(models.Model):

    title = models.CharField(max_length=100)
    header_text = models.TextField()
    body_text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='ot')
    tag = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, 
        blank=True, null=True,
        width_field="width_field",
        height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    slug = models.SlugField(max_length=100, unique=True)

    # auto_now_add is when the model is created; auto_now is at any time whatever; so this is only done once
    # an updated field would be almost the same, but reversed
    # blank in the form, null in the database

    def __str__(self):
        return str(self.title + ': ' + self.category)


    def save(self, *args, **kwargs):
    	self.slug = uuslug(self.title, instance=self, max_length=100)
    	super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:post", kwargs={"slug": self.slug})
        # return reverse("posts:detail", kwargs={"id": self.id})

    def get_markdown_header_text(self):
        content = self.header_text
        return markdown(content)

    def get_markdown_body_text(self):
        content = self.body_text 
        return markdown(content)

    class Meta:
        ordering=["created_date", "-updated"]

# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.title)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Post.objects.filter(slug=slug).order_by("-id")
#     exists = qs.exists()
#     if exists:
#         new_slug_ = "%s-%s" %(slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug

# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)
#     # slug = slugify(instance.title)
#     # exists = Post.objects.filter(slug=slug).exists()
#     # if exists:
#     #     slug = "%s-%s" %(slug, instance.id)
#     # instance.slug = slug

# pre_save.connect(pre_save_post_receiver, sender=Post)