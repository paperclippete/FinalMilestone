from django.test import TestCase
from django.shortcuts import reverse, redirect
from django.contrib.auth.models import User
from events.models import Event
from membership.models import Membership

# Create your tests here.


class TestSearchViews(TestCase):
    def test_get_all_events_page_redirect(self):
        """ Test search redirects to index with an empty result(or database)"""
        page = self.client.get("/search/")
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse("index"))

    def test_get_all_events_page(self):
        """ Test search renders correct template with events in db """
        test_user = User.objects.create(username="TestUser",
                                        password="TestPassword")
        membership = Membership.objects.create(user_id='1')
        self.client.force_login(test_user)
        test_event = Event.objects.create(
                title="TestEvent",
                description="Test Event Works",
                price=None,
                age_range="Adults",
                address="70 Castle Street",
                town="Hamilton",
                post_code="ML3 3PU",
                event_type="Arts and Crafts",
                event_date_begins="2019-10-31",
                event_date_ends="2019-10-31",
                event_time_begins="18:00:00",
                event_time_ends="19:00:00",
                event_day="Tuesday",
                max_participants="25",
                event_host=test_user,
                image=None
            )
        page = self.client.get("/search/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "view_all_events.html")
