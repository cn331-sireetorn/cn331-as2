from pydoc import resolve
from urllib import response
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from login.views import index, login_view, logout_view

# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_index_url_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_login_url_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_view)

    def test_logout_url_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_view)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.username = 'username'
        self.password = 'password'
        self.email = 'user@gmail.com'
        self.fname = 'first'
        self.lname = 'last'
        self.credentials = {
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'first_name': self.fname,
            'last_name': self.lname}
        self.user = User.objects.create_user(**self.credentials)

        self.index_url = reverse('index')
        self.login_view_url = reverse('login')
        self.logout_view_url = reverse('logout')
        
    def test_index_GET(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/index.html')

    def test_login_view_GET(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.login_view_url)

        self.assertEquals(response.status_code, 400)
        self.assertTemplateUsed(response, 'login/login.html')
    
    def test_login_view_POST(self):
        # login incomplete
        credentials = {
            'username': 'user',
            'password': 'pass',
        }
        response = self.client.post(self.login_view_url, credentials, follow=True)

        self.assertFalse(response.context['user'].is_active)
        self.assertEquals(response.status_code, 400)
        self.assertTemplateUsed(response, 'login/login.html')

    def test_login_view_POST_success(self):
        # login complete
        response = self.client.post(self.login_view_url, self.credentials, follow=True)

        self.assertTrue(response.context['user'].is_active)
        self.assertTemplateUsed(response, 'login/index.html')

        self.client.login(username=self.username, password=self.password)
        response = self.client.post(self.login_view_url, {
            'username':self.username, 
            'password': self.password
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/index.html')

    def test_logout_view_GET(self):
        response = self.client.get(self.logout_view_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')
