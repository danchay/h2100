from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from .views import about
from blog.models import Post

class AboutPageTest(TestCase):

	# # Resolve / URL to index view? Import resolve
	# # Make view function return HTML import blog.views index
	# def test_root_url_resolves_to_index_view(self):
	# 	found = resolve('/')
	# 	self.assertEqual(found.func, index)

	def test_about_page_resolves_to_correct_view(self):
		found = resolve('/about-this-site/')
		self.assertEqual(found.func, about)

		about_test = Post()
		about_test.title = 'About this site'
		about_test.slug = 'about-this-site'
		about_test.body = 'This is the body.'
		about_test.save()
		saved_items = Post.objects.all()
		self.assertEqual(saved_items.count(), 1)
		about_saved_item = saved_items[0]
		self.assertEqual(about_saved_item.title, 'About this site')



		# # request = HttpRequest()
		# # response = about(request)
		response = self.client.get('/about-this-site/')

		# # # html = response.content.decode('utf8')
		# # # # self.assertIn('<html lang="en">', html)
		# # # # self.assertIn('<title>H2100</title>', html)
		# # # # self.assertIn('favicon-32x32.png', html)
		# # # # self.assertIn('</html>', html)
		# # # self.assertIn('<h1>About this site</h1>', html)
		# # # self.assertTrue(html.strip().endswith('</html>'))
		self.assertTemplateUsed(response, 'about.html')


# class SmokeTest(TestCase):

# 	def test_bad_math(self):
# 		self.assertEqual(1 + 1, 3)

