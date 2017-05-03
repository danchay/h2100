from selenium.webdriver.common.keys import Keys 
from .base import FunctionalTest
from selenium.common.exceptions import WebDriverException
import time

class Search(FunctionalTest):

	def test_search(self):
		self.browser.get('http://localhost:8000')
		# # She is invited to search titles and tags in a search form
		search_input_box = self.browser.find_element_by_class_name('form-control')
		self.assertEqual(search_input_box.get_attribute('placeholder'), 'Search in titles and tags')

		# # She does a search on the first listed post
		search_item = self.browser.find_element_by_xpath("//div[@class='col-md-8']/ul/h2/a")
		self.assertTrue(search_item)
		self.assertTrue(search_item.text)
		search_item=search_item.text
		search_input_box.send_keys(search_item)
		search_input_box.send_keys(Keys.ENTER)
		time.sleep(1)
		new_header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Search Results', new_header_text)
		self.assertTrue(search_item)

		# # She clicks on a post title and it returns a single post with Tag:
		post_title = search_item
		post_title_link = self.browser.find_element_by_link_text(post_title)
		post_title_link.click()
		time.sleep(1)

		tag = self.browser.find_element_by_css_selector("p.pull-right").text
		self.assertIn('Tag:', tag)


#Following conditional not needed when using Django test runner
if __name__ == '__main__':
	unittest.main()

