from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.

class LoginPageViewTest(TestCase):
    def test_login_page_view_url(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_view_template_used(self):
        response = self.client.get('/accounts/login/')
        self.assertTemplateUsed(response, 'account/login.html')

    def test_login_page_view_content(self):
        response = self.client.get('/accounts/login/')
        self.assertContains(response, 'Login')

class SignupPageViewTest(TestCase):
    def test_signup_page_view_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_page_view_template_used(self):
        response = self.client.get('/accounts/signup/')
        self.assertTemplateUsed(response, 'account/signup.html')

    def test_signup_page_view_content(self):
        response = self.client.get('/accounts/signup/')
        self.assertContains(response, 'Sign Up')

# class LogoutPageViewTest(TestCase):
#     def test_logout_page_view_url(self):
#         response = self.client.get('/accounts/logout/')
#         self.assertEqual(response.status_code, 200)
#
#     def test_logout_page_view_template_used(self):
#         response = self.client.get('/accounts/logout/')
#         self.assertTemplateUsed(response, 'account/logout.html')
#
#     def test_logout_page_view_content(self):
#         response = self.client.get('/accounts/logout/')
#         self.assertContains(response, 'Logout')