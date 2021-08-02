from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class FormTestCase(TestCase):
    fixtures = ["fixtures/init.json"]
    def setUp(self) -> None:

        self.headers = {'Content-Type': 'application/json'}
        self.user_profile = {
            'User_name': 'name',
            'User_email': 'aq@aq.ru',
            'User_phone': '79188962231',
            'User_date': '28.07.2021'
        }

        self.user = {
            'User_name': 'name',
            'User_email': 'aq@aq.ru',
            'User_phone': '79188962231',
        }
        self.no_form ={
            'User_name': 'name',
            'User_email': 'aq@aq.ru',
        }

        self.login = {
            'User_name': 'name',
        }

    def test_form_user_profile(self):
        response = self.client.get(reverse('template'),  data=self.user_profile, headers=self.headers, secure=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code, msg='status_200')
        self.assertJSONEqual(response.content, {"name": "User_profile"})


    def test_form_user(self):
        response = self.client.get(reverse('template'), data=self.user, headers=self.headers, secure=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code, msg='status_200')
        self.assertJSONEqual(response.content, {"name": "User"})


    def test_form_login(self):
        response = self.client.get(reverse('template'), data=self.login, headers=self.headers, secure=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code, msg='status_200')
        self.assertJSONEqual(response.content, {"name": "User_login"})


    def test_no_form_in_base(self):
        response = self.client.get(reverse('template'), data=self.no_form, headers=self.headers, secure=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code, msg='status_200')
        self.assertJSONEqual(response.content, {'User_name': 'text','User_email': 'email'})

