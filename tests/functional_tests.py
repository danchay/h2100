from selenium import webdriver 
import unittest

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
		self.fail('Finish the test.')

# She notice the logo image

# She notices 'Hacking to 100'

# She notices '...xxxx days pending.' in the nav bar

# She notices a quotation at the top of the front page

# She is invited to search titles and tags in a search form

# She notices 'Most Popular Posts' w/ 5 links

# She notices the Dan Chay email address

# She sees that there is a list of post items

# She sees 'Page x of x. Next'

# She does a search and it returns a list of posts

# She clicks on a post title and it returns a single post


if __name__ == '__main__':
	unittest.main()