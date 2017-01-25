from django.test import TestCase
from blog.models import Post 


class PostTests(TestCase):

    def test_str(self):
        my_title = Post(title='Title basic test case')

        self.assertEquals(
            str(my_title), 'Title basic test case',
        )
