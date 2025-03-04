from django.contrib.auth.models import User
from django.urls import resolve, reverse
from django.test import TestCase
from ..views import signup
from ..forms import SignUpForm
from django.contrib.auth import get_user_model
class SignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    # def test_signup_status_code(self):
    #     url = reverse('signup')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    # def test_signup_url_resolves_signup_view(self):
    #     view = resolve('/signup/')
    #     self.assertEqual(view.func, signup)
        
    # def test_csrf(self):
    #     self.assertContains(self.response, 'csrfmiddlewaretoken')

    # def test_contains_form(self):
    #     form = self.response.context.get('form')
    #     self.assertIsInstance(form, SignUpForm)
    # def test_form_inputs(self):
    #     '''
    #     The view must contain five inputs: csrf, username, email,
    #     password1, password2
    #     '''
    #     self.assertContains(self.response, '<input', 5)
    #     self.assertContains(self.response, 'type="text"', 1)
    #     self.assertContains(self.response, 'type="email"', 1)
    #     self.assertContains(self.response, 'type="password"', 2)


class SuccessfulSignUpTests(TestCase):
    
    def setUp(self):
        self.signup_url = reverse('signup')
        self.home_url = reverse('home')
        self.user_data = {
            'username': 'john',
            'email': 'john@doe.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
        self.response = self.client.post(self.signup_url, self.user_data)

    def test_redirection(self):
        '''
        A valid form submission should redirect the user to the home page.
        '''
        self.assertRedirects(self.response, self.home_url)

    def test_user_creation(self):
        '''
        A valid form submission should create a new user.
        '''
        User = get_user_model()
        self.assertTrue(User.objects.filter(username='john').exists())

    def test_user_authentication(self):
        '''
        After a successful signup, the user should be authenticated.
        '''
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


class InvalidSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.post(url, {})  # submit an empty dictionary

    # def test_signup_status_code(self):
    #     '''
    #     An invalid form submission should return to the same page
    #     '''
    #     self.assertEqual(self.response.status_code, 200)

    # def test_form_errors(self):
    #     form = self.response.context.get('form')
    #     self.assertTrue(form.errors)

    # def test_dont_create_user(self):
    #     User = get_user_model()
    #     self.assertFalse(User.objects.exists())