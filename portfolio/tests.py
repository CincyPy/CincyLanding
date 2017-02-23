from django.test import TestCase
from selenium import webdriver


# Create your tests here.
class UrlTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_url(self):
        self.browser.get('http://localhost:8000/home/')
        self.assertIn('Start', self.browser.title)

    def test_portfolio_url(self):
        self.browser.get('http://localhost:8000/portfolio/')
        self.assertIn('Start', self.browser.title)

    def test_admin_url(self):
        self.browser.get('http://localhost:8000/admin/')
        self.assertIn('admin', self.browser.title)

