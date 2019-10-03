from django.test import TestCase

# Test Accounts Views

class TestHomeViews(TestCase):
    """ Test each page loads with correct template """
    def test_get_index_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        
    def test_get_about_us_page(self):
        page = self.client.get("/about_us/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "about_us.html")