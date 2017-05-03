
from selenium.webdriver.common.keys import Keys 
from .base import FunctionalTest



class Ckwotes(FunctionalTest):

	def test_ckwote_render(self):
		self.browser.get('http://localhost:8000')
		# # She notices a quotation at the top of the front page
		ckwote = self.browser.find_element_by_tag_name('em').text 
		self.assertTrue(ckwote.startswith('"'))
		self.assertIn('"', ckwote)
		self.assertTrue(len(ckwote) > 10)


#Following conditional not needed when using Django test runner
if __name__ == '__main__':
	unittest.main()

