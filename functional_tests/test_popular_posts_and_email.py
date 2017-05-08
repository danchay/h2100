from selenium.webdriver.common.keys import Keys 
from .base import FunctionalTest

class PopularPostsAndEmail(FunctionalTest):

	def test_popular_posts_and_email(self):
		self.browser.get('http://localhost:8000')
		# # She notices 'Most Popular Posts' w/ 5 links
		mp_posts = self.browser.find_element_by_tag_name('h4').text 
		self.assertIn('Most Popular Posts', mp_posts)

		# # She notices the Dan Chay email address
		email = self.browser.find_element_by_tag_name('address').text 
		self.assertIn('Dan Chay', email)

#Following conditional not needed when using Django test runner
if __name__ == '__main__':
	unittest.main()

