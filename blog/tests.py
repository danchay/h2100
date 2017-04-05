from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from blog.views import index, healthspan, training, eating, sleeping, learning, other, post


class IndexPageTest(TestCase):

	# Resolve / URL to index view? Import resolve
	# Make view function return HTML import blog.views index
	# def test_root_url_resolves_to_index_view(self):
	# 	found = resolve('/')
	# 	self.assertEqual(found.func, index)

	# Import HttpRequest
	def test_index_page_returns_correct_html(self):
		# request = HttpRequest()
		# response = index(request)
		response = self.client.get('/')

		html = response.content.decode('utf8')
		self.assertIn('<html lang="en">', html)
		self.assertIn('<title>H2100</title>', html)
		self.assertIn('favicon-32x32.png', html)
		self.assertIn('</html>', html)
		self.assertTrue(html.strip().endswith('</html>'))
		self.assertTemplateUsed(response, 'blog/index.html')

	def test_index_page_displays_ckwote_in_html(self):
		request = HttpRequest()
		response = index(request)
		html = response.content.decode('utf8')
		self.assertIn('"', html)

	def test_index_page_displays_search_form_in_html(self):
		request = HttpRequest()
		response = index(request)
		html = response.content.decode('utf8')
		self.assertIn('Search in titles and tags', html)

	def test_index_page_displays_email_in_html(self):
		request = HttpRequest()
		response = index(request)
		html = response.content.decode('utf8')
		self.assertIn('Dan Chay', html)


class CategoryPageTests(TestCase):

	def test_healthspan_url_resolves_to_healthspan_view(self):
		found = resolve('/blog/healthspan/')
		self.assertEqual(found.func, healthspan)

	def test_training_url_resolves_to_training_view(self):
		found = resolve('/blog/training/')
		self.assertEqual(found.func, training)

	def test_eating_url_resolves_to_eating_view(self):
		found = resolve('/blog/eating/')
		self.assertEqual(found.func, eating)

	def test_sleeping_url_resolves_to_sleeping_view(self):
		found = resolve('/blog/sleeping/')
		self.assertEqual(found.func, sleeping)

	def test_learning_url_resolves_to_learning_view(self):
		found = resolve('/blog/learning/')
		self.assertEqual(found.func, learning)

	def test_other_url_resolves_to_other_view(self):
		found = resolve('/blog/other/')
		self.assertEqual(found.func, other)




# Test tests.py
# class SmokeTest(TestCase):

# 	def test_bad_math(self):
# 		self.assertEqual(1 + 1, 2)

