from django.test import TestCase
from accounts.forms import UserLoginForm, UserRegistrationForm

# Create your tests here.

# Testing Accounts Forms

# Test User Login Form is valid and provides correct errors
class TestUserLoginForm(TestCase):
    def test_log_in_valid(self):
        form = UserLoginForm(
            {"username": "TestUser", "password": "TestPassword"})
        self.assertTrue(form.is_valid())

    def test_correct_error_message(self):
        form = UserLoginForm({"username": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["username"], [u"This field is required."])


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
