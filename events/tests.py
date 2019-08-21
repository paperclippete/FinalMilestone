from django.test import TestCase
from django.shortcuts import reverse
from .forms import CreateEventForm


# Testing Create Event Form

# Test Form is valid and provides correct errors

class TestCreateEventForm(TestCase):
    def test_event_is_valid(self):
        form = CreateEventForm(
            {
                "title": "TestEvent", 
                "description": "Test Event Works",
                "price": None,
                "age_range": "Babies and Toddlers",
                "town": "Hamilton",
                "address": "70 Castle Street",
                "post_code": "ML3 3PU",
                "event_type": "Health and Wellbeing",
                "event_date": "21-08-2019",
                "event_time": "18:00",
                "event_host": "admin",
                "max_participants": 25,
                "image": None
            })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["event_host"], [u""])
        
        
# Test Event Views

# Test each page loads with correct template
# class TestViews(TestCase):
#     def test_get_login_page(self):
#         page = self.client.get("/accounts/login/")
#         self.assertEqual(page.status_code, 200)
#         self.assertTemplateUsed(page, "login.html")
        