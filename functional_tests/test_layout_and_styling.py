from selenium.webdriver.common.keys import Keys 
from .base import FunctionalTest



class LayoutAndStylingTest(FunctionalTest):		

	def test_header_elements_render(self):
		# She opens homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title
		self.assertIn('H2100', self.browser.title)
		
		# She notices the logo image
		logo = self.browser.find_element_by_css_selector("img[src$='favicon-32x32.png'].navbar-brand")
		self.assertTrue(logo)

		# # She notices 'Hacking to 100'
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Hacking to 100', header_text)


#Following conditional not needed when using Django test runner
if __name__ == '__main__':
	unittest.main()

