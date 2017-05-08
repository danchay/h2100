from selenium.webdriver.common.keys import Keys 
from .base import FunctionalTest		


class PageNumbering(FunctionalTest):

	def test_page_numbering(self):
		self.browser.get('http://localhost:8000')
		# # She sees 'Page x of x. Next'
		pages = self.browser.find_element_by_class_name('current').text
		self.assertIn('Page', pages)

#Following conditional not needed when using Django test runner
if __name__ == '__main__':
	unittest.main()

