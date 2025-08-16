from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class AuthFlowTests(TestCase):
    def test_register_login_profile(self):
        # Register
        resp = self.client.post(reverse('register'), {
            'username': 'goodnews',
            'email': 'goodnewskeyz',
            'password1': '',
            'password2': 'StrongPass123!',
        })
        self.assertRedirects(resp, reverse('login'))

        # Login
        resp = self.client.post(reverse('login'), {
            'username': 'goodnews',
            'password': 'StrongPass123!'
        })
        self.assertRedirects(resp, reverse('profile'))

        # View profile
        resp = self.client.get(reverse('profile'))
        self.assertEqual(resp.status_code, 200)

        # Update profile
        resp = self.client.post(reverse('profile'), {
            'username': '

# Create your tests here.
