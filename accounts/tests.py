from django.test import TestCase
from django.shortcuts import reverse
from .forms import UserLoginForm, UserRegistrationForm

# Testing Accounts Forms

# Test User Login Form is valid and provides correct errors
class TestUserLoginForm(TestCase):
    def test_log_in_valid(self):
        form = UserLoginForm({"username_or_email": "TestUser", "password": "TestPassword"})
        self.assertTrue(form.is_valid())

    def test_correct_error_message(self):
        form = UserLoginForm({"username": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["username_or_email"], [u"This field is required."])


# Test User Registration Form is valid and provides correct errors
class TestUserRegistrationForm(TestCase):
    def test_register_form_valid(self):
        form = UserRegistrationForm(
            {"username": "TestUser", "email": "Test@Email.com",
                "first_name": "TestFirstName", "last_name": "TestLastName",
                "password1": "TestPassword", "password2": "TestPassword"})
        self.assertTrue(form.is_valid())

    def test_passwords_do_not_match(self):
        form = UserRegistrationForm(
            {"username": "TestUser", "email": "Test@Email.com",
                "first_name": "TestFirstName", "last_name": "TestLastName",
                "password1": "TestPassword", "password2": "TestPass"})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["password2"], [u"The two password fields didn't match."])
            
# Test Accounts Views

# Test each page loads with correct template
class TestViews(TestCase):
    # Will no longer work with login modal
    def test_get_login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        

    def test_get_registration_page(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "register.html")
        

    def test_get_profile_page(self):
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse("login"))
    
    def test_logout_view(self):
        page = self.client.get("/accounts/logout/")
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse("index"))
