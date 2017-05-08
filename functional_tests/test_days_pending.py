from selenium.webdriver.common.keys import Keys 
from .base import FunctionalTest

class DaysPending(FunctionalTest):

	def test_days_pending_render(self):
		self.browser.get('http://localhost:8000')
		# # She notices '...xxxx days pending.' in the nav bar
		# # The string will be longer than 18 elements long if digits in number days > 2
		days_pending = self.browser.find_element_by_xpath("//div[@class='navbar-header']/span[contains(text(), 'days pending.')]")
		self.assertTrue(len(days_pending.text) > 18)

#Following conditional not needed when using Django test runner
if __name__ == '__main__':
	unittest.main()

