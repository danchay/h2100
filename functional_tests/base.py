import unittest
from unittest import skip
from django.test import LiveServerTestCase, TestCase
from selenium import webdriver 
from selenium.common.exceptions import WebDriverException
import time



MAX_WAIT = 10


class FunctionalTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_browser_render(self):
		# She opens homepage
		self.browser.get('http://localhost:8000')		



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
