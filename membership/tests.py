from django.test import TestCase, Client
from django.shortcuts import reverse
from django.contrib import auth
from .forms import OrderMembershipForm
from django.contrib.auth.models import User
from .models import Membership

# Testing Membership Forms

class TestOrderMembershipForm(TestCase):
    """ Test Order Membership Form is valid and provides correct errors """
    def test_order_form_valid(self):
        test_user = User.objects.create(username="TestUser", password="TestPassword")
        membership = Membership.objects.create(user_id='1')
        membership_level = 'bronze'
        self.client.force_login(test_user)
        form = OrderMembershipForm({
            "first_name": "TestName",
            "last_name": "TestLast",
            "town_or_city": "Hamilton",
            "street_address1": "67 Lockhart Street",
            "street_address2": "",
            "postcode": "ML3 6PU"
        })
        self.assertTrue(form.is_valid())
        
    def test_order_form_not_valid(self):
        test_user = User.objects.create(username="TestUser", password="TestPassword")
        membership = Membership.objects.create(user_id='1')
        membership_level = 'bronze'
        self.client.force_login(test_user)
        form = OrderMembershipForm({
            "first_name": "TestName",
            "last_name": "TestLast",
            "town_or_city": "Hamilton",
            "street_address1": "67 Lockhart Street",
            "street_address2": "",
            "postcode": ""
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["postcode"], [u"This field is required."])


# Test Membership Views

class TestMembershipViews(TestCase):
    """ Test Upgrade Membership Form is displayed """
    def test_get_profile_page(self):
        test_user = User.objects.create(username="TestUser", password="TestPassword")
        membership = Membership.objects.create(user_id='1')
        self.client.force_login(test_user)
        page = self.client.get("/membership/upgrade/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "membership.html")