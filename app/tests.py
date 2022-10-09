from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user

class MyTestCase(TestCase):
    def test_login(self):
        self.client.login(username='fred', password='secret')
        self.assertTrue(get_user(self.client))