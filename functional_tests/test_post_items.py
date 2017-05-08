from selenium.webdriver.common.keys import Keys 
from .base import FunctionalTest

class PostItems(FunctionalTest):

	def test_post_items(self):
		self.browser.get('http://localhost:8000')
		# # She sees that there is a list of post items
		posts = self.browser.find_elements_by_class_name('post-item')
		self.assertTrue(len(posts) >= 1)
		self.assertFalse(len(posts) >= 5)

#Following conditional not needed when using Django test runner
if __name__ == '__main__':
	unittest.main()

