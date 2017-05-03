
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import WebDriverException
import time


class NewVisitorsTest(StaticLiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_page_elements_render(self):
		self.browser.get(self.live_server_url)
		#time.sleep(3)
		self.assertIn('H2100', self.browser.title)
		

	def test_logo_render(self):
		self.browser.get(self.live_server_url)
		logo = self.browser.find_element_by_css_selector("img[src$='static/img/favicon-32x32.png'].navbar-brand")		
		#time.sleep(3)
		self.assertTrue(logo)
		

	# def test_header_text_render(self):
	# 	self.browser.get(self.live_server_url)
	# 	header_text = self.browser.find_element_by_tag_name('h1').text
	# 	time.sleep(3)
	# 	self.assertIn('Hacking to 100', header_text)