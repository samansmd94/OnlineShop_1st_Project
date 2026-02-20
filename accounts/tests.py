from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.

class LoginPageViewTest(TestCase):
    def test_login_page_view_url_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_view_template_used(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_page_view_content(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'Login')

class SignupPageViewTest(TestCase):
    def test_signup_page_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_view_template_used(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_page_view_content(self):
        response = self.client.get(reverse('signup'))
        self.assertContains(response, 'Sign Up')