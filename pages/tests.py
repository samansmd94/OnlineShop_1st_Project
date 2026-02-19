from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.

class HomePageViewTest(TestCase):
    def test_home_page_view_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_view_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Home Page')

class AboutPageViewTest(TestCase):
    def test_about_page_view_url(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_view_url_by_name(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_view_content(self):
        response = self.client.get(reverse('aboutus'))
        self.assertContains(response, 'About Us')

