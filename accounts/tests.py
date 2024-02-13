from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignUpPageTest(TestCase):
    username = 'username'
    email = 'myusername@gmail.com'
    age = 22

    def test_signup_page_by_name_url(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        user = get_user_model().objects.create_user(
            username='username',
            email='myusername@gmail.com',
            age=22,
        )
        self.assertEqual(get_user_model().objects.count(), 1, )
        self.assertEqual(get_user_model().objects.all()[0].username, user.username)
        self.assertEqual(get_user_model().objects.all()[0].email, user.email)
        self.assertEqual(get_user_model().objects.all()[0].age, user.age)
