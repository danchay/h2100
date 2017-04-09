import unittest
from django.test import LiveServerTestCase, TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import WebDriverException
import time


MAX_WAIT = 10


		


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_page_elements_render(self):
		# She opens homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title
		self.assertIn('H2100', self.browser.title)
		
		# She notices the logo image
		logo = self.browser.find_element_by_css_selector("img[src$='favicon-32x32.png'].navbar-brand")
		self.assertTrue(logo)

		# # She notices 'Hacking to 100'
		# header_text = self.browser.find_element_by_tag_name('h1').text
		# self.assertIn('Hacking to 100', header_text)

		# # She notices '...xxxx days pending.' in the nav bar
		# # The string will be longer than 18 elements long if digits in number days > 2
		# days_pending = self.browser.find_element_by_xpath("//div[@class='navbar-header']/span[contains(text(), 'days pending.')]")
		# self.assertTrue(len(days_pending.text) > 18)

		# # She notices a quotation at the top of the front page
		# ckwote = self.browser.find_element_by_tag_name('em').text 
		# self.assertTrue(ckwote.startswith('"'))
		# self.assertIn('"', ckwote)
		# self.assertTrue(len(ckwote) > 10)

		# # She notices 'Most Popular Posts' w/ 5 links
		# mp_posts = self.browser.find_element_by_tag_name('h4').text 
		# self.assertIn('Most Popular Posts', mp_posts)

		# # She notices the Dan Chay email address
		# email = self.browser.find_element_by_tag_name('address').text 
		# self.assertIn('Dan Chay', email)

		# # She sees that there is a list of post items
		# posts = self.browser.find_elements_by_class_name('post-item')
		# self.assertTrue(len(posts) >= 1)
		# self.assertFalse(len(posts) >= 5)

		# # She sees 'Page x of x. Next'
		# pages = self.browser.find_element_by_class_name('current').text
		# self.assertIn('Page', pages)

		# # She is invited to search titles and tags in a search form
		# search_input_box = self.browser.find_element_by_class_name('form-control')
		# self.assertEqual(search_input_box.get_attribute('placeholder'), 'Search in titles and tags')

		# # She does a search on the first listed post
		# search_item = self.browser.find_element_by_xpath("//div[@class='col-md-8']/ul/h2/a")
		# self.assertTrue(search_item)
		# self.assertTrue(search_item.text)
		# search_item=search_item.text
		# search_input_box.send_keys(search_item)
		# search_input_box.send_keys(Keys.ENTER)
		# time.sleep(1)
		# new_header_text = self.browser.find_element_by_tag_name('h1').text
		# self.assertIn('Search Results', new_header_text)
		# self.assertTrue(search_item)

		# # She clicks on a post title and it returns a single post with Tag:
		# post_title = search_item
		# post_title_link = self.browser.find_element_by_link_text(post_title)
		# post_title_link.click()
		# time.sleep(1)

		# tag = self.browser.find_element_by_css_selector("p.pull-right").text
		# self.assertIn('Tag:', tag)





		# self.fail('Finish the test.')

#Following conditional not needed when using Django test runner
if __name__ == '__main__':
	unittest.main()



#########################
# def wait_for_execution(test_obj):
# 	start_time = time.time()
# 	while True:
# 		try:
# 			test_obj
# 			return 
# 		except (AssertionError, WebDriverException) as e:
# 			if time.time() -start_time > MAX_WAIT:
# 				raise e 
# 			time.sleep(0.5)


# class NewVisitorTest(StaticLiveServerTestCase):

# 	def setUp(self):
# 		self.browser = webdriver.Firefox()

# 	def tearDown(self):
# 		self.browser.quit()

# 	def test_page_elements_render(self):
# 		self.browser.get(self.live_server_url)
# 		time.sleep(3)
# 		self.assertIn('H2100', self.browser.title)
		

# 	def test_logo_render(self):
# 		logo = self.browser.find_element_by_css_selector("img[src$='static/img/favicon-32x32.png'].navbar-brand")		
# 		time.sleep(3)
# 		self.assertTrue(logo)
		

# 	def test_header_text_render(self):
# 		header_text = self.browser.find_element_by_tag_name('h1').text
# 		time.sleep(3)
# 		self.assertIn('Hacking to 100', header_text)