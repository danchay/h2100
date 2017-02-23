from django.db import models

from uuslug import uuslug

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

class Post(models.Model):

    title = models.CharField(max_length=100)
    header_text = models.TextField()
    body_text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='ot')
    tag = models.CharField(max_length=20, blank=True, null=True)
    image=models.ImageField(upload_to="images", blank=True, null=True)
    views=models.IntegerField(default=0)
    slug = models.CharField(max_length=100, unique=True)

    # auto_now_add is when the model is created; auto_now is at any time whatever; so this is only done once
    # an updated field would be almost the same, but reversed
    # blank in the form, null in the database

    def __str__(self):
        return str(self.title + ': ' + self.category)


    def save(self, *args, **kwargs):
    	self.slug = uuslug(self.title, instance=self, max_length=100)
    	super(Post, self).save(*args, **kwargs)

