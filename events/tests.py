from django.test import TestCase
from django.shortcuts import reverse, redirect
from django.contrib.auth.models import User
from membership.models import Membership
from .models import Event, Participant, Like
from .forms import CreateEventForm, LikeEvent


class TestCreateEventForm(TestCase):
    """ Test Event Form is valid or displays correct errors"""
    def test_event_is_valid(self):
        test_user = User.objects.create(username="TestUser", password="TestPassword")
        membership = Membership.objects.create(user_id='1')
        self.client.force_login(test_user)
        form = CreateEventForm(
            {
                "title": "TestEvent", 
                "description": "Test Event Works",
                "price": None,
                "age_range": "Adults",
                "address": "70 Castle Street",
                "town": "Hamilton",
                "post_code": "ML3 3PU",
                "event_type": "Arts and Crafts",
                "event_date_begins": "30/10/2019",
                "event_date_ends": "31/10/2019",
                "event_time_begins": "18:00",
                "event_time_ends": "19:00",
                "event_day": "Tuesday",
                "max_participants": '25',
                "image": None
            })
        self.assertTrue(form.is_valid())
        
    def test_event_is_not_valid(self):
        test_user = User.objects.create(username="TestUser", password="TestPassword")
        membership = Membership.objects.create(user_id='1')
        self.client.force_login(test_user)
        form = CreateEventForm(
            {
                "title": None, 
                "description": "Test Event Works",
                "price": None,
                "age_range": "",
                "address": "70 Castle Street",
                "town": "Hamilton",
                "post_code": "ML3 3PU",
                "event_type": "Arts and Crafts",
                "event_date_begins": "30/10/2019",
                "event_date_ends": "31/10/2019",
                "event_time_begins": "18:00",
                "event_time_ends": "19:00",
                "event_day": "Tuesday",
                "max_participants": '25',
                "image": None
            })
        self.assertFalse(form.is_valid())    
        self.assertEqual(
            form.errors["title"], [u"This field is required."])

# Test Views

class TestEventViews(TestCase):
    """ Test Events Views """
    def test_get_post_event_page_redirect(self):
        page = self.client.get("/events/post_event/")
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse("index"))
        
    def test_get_post_event_page(self):
        """ Test post event page renders correct template """
        test_user = User.objects.create(username="TestUser", password="TestPassword")
        membership = Membership.objects.create(user_id='1')
        self.client.force_login(test_user)
        page = self.client.get("/events/post_event/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "post_event.html")
        
    def test_get_edit_event_page(self):
        """ Test edit event page renders correct template """
        test_user = User.objects.create(username="TestUser", password="TestPassword")
        self.client.force_login(test_user)
        test_event = Event.objects.create(
                title= "TestEvent", 
                description= "Test Event Works",
                price= None,
                age_range= "Adults",
                address= "70 Castle Street",
                town= "Hamilton",
                post_code= "ML3 3PU",
                event_type= "Arts and Crafts",
                event_date_begins= "2019-10-31",
                event_date_ends= "2019-10-31",
                event_time_begins= "18:00:00",
                event_time_ends= "19:00:00",
                event_day= "Tuesday",
                max_participants= "25",
                event_host= test_user,
                image= None
            )
        page = self.client.get("/events/view_one_event/edit_event/{0}".format(test_event.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "post_event.html")

    def test_get_all_events_page_redirect(self):
        """ Test search redirects to index with an empty result(or database) """
        page = self.client.get("/search/")
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse("index"))
        
    def test_get_all_events_page(self):
        """ Test search renders correct template with events in db """
        test_user = User.objects.create(username="TestUser", password="TestPassword")
        membership = Membership.objects.create(user_id='1')
        self.client.force_login(test_user)
        test_event = Event.objects.create(
                title= "TestEvent", 
                description= "Test Event Works",
                price= None,
                age_range= "Adults",
                address= "70 Castle Street",
                town= "Hamilton",
                post_code= "ML3 3PU",
                event_type= "Arts and Crafts",
                event_date_begins= "2019-10-31",
                event_date_ends= "2019-10-31",
                event_time_begins= "18:00:00",
                event_time_ends= "19:00:00",
                event_day= "Tuesday",
                max_participants= "25",
                event_host= test_user,
                image= None
            )
        page = self.client.get("/search/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "view_all_events.html")
        
    
    def test_get_one_event_page(self):
        """ Test one event renders correct template """
        test_user = User.objects.create(username="TestUser", password="TestPassword")
        self.client.force_login(test_user)
        test_event = Event.objects.create(
                title= "TestEvent", 
                description= "Test Event Works",
                price= None,
                age_range= "Adults",
                address= "70 Castle Street",
                town= "Hamilton",
                post_code= "ML3 3PU",
                event_type= "Arts and Crafts",
                event_date_begins= "2019-10-31",
                event_date_ends= "2019-10-31",
                event_time_begins= "18:00:00",
                event_time_ends= "19:00:00",
                event_day= "Tuesday",
                max_participants= "25",
                event_host= test_user,
                image= None
            )
        page = self.client.get("/events/view_one_event/{0}".format(test_event.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "view_one_event.html")
        
    def test_get_one_event_page_404(self):
        """ Tests an unknown id provides a 404 error """
        test_user = User.objects.create(username="TestUser", password="TestPassword")
        self.client.force_login(test_user)
        page = self.client.get("/events/view_one_event/3")
        self.assertEqual(page.status_code, 404)
        self.assertTemplateUsed(page, "404.html")

    def test_delete_one_event(self):
        test_user = User.objects.create(username="TestUser", password="TestPassword")
        membership = Membership.objects.create(user_id='1')
        self.client.force_login(test_user)
        test_event = Event.objects.create(
                title= "TestEvent", 
                description= "Test Event Works",
                price= None,
                age_range= "Adults",
                address= "70 Castle Street",
                town= "Hamilton",
                post_code= "ML3 3PU",
                event_type= "Arts and Crafts",
                event_date_begins= "2019-10-31",
                event_date_ends= "2019-10-31",
                event_time_begins= "18:00:00",
                event_time_ends= "19:00:00",
                event_day= "Tuesday",
                max_participants= "25",
                event_host= test_user,
                image= None
            )
        page = self.client.get("/events/view_one_event/delete_event/{0}".format(test_event.id))
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse("user_profile"))
        
    def test_delete_participant(self):
        test_user = User.objects.create(username="TestUser", password="TestPassword")
        test_event = Event.objects.create(
                title= "TestEvent", 
                description= "Test Event Works",
                price= None,
                age_range= "Adults",
                address= "70 Castle Street",
                town= "Hamilton",
                post_code= "ML3 3PU",
                event_type= "Arts and Crafts",
                event_date_begins= "2019-10-31",
                event_date_ends= "2019-10-31",
                event_time_begins= "18:00:00",
                event_time_ends= "19:00:00",
                event_day= "Tuesday",
                max_participants= "25",
                event_host= test_user,
                image= None
            )        
        participant = Participant.objects.create(user_id='1', event_id='1')
        self.client.force_login(test_user)
        page = self.client.get("/events/view_one_event/delete_participant/{0}".format(participant.id))
        self.assertEqual(page.status_code, 302)
        self.client.post(redirect("search"))
        
    def test_delete_like(self):
        test_user = User.objects.create(username="TestUser", password="TestPassword")
        test_event = Event.objects.create(
                title= "TestEvent", 
                description= "Test Event Works",
                price= None,
                age_range= "Adults",
                address= "70 Castle Street",
                town= "Hamilton",
                post_code= "ML3 3PU",
                event_type= "Arts and Crafts",
                event_date_begins= "2019-10-31",
                event_date_ends= "2019-10-31",
                event_time_begins= "18:00:00",
                event_time_ends= "19:00:00",
                event_day= "Tuesday",
                max_participants= "25",
                event_host= test_user,
                image= None
            )        
        like = Like.objects.create(user_id='1', event_id='1')
        self.client.force_login(test_user)
        page = self.client.get("/events/view_one_event/delete_like/{0}".format(like.id))
        self.assertEqual(page.status_code, 302)

