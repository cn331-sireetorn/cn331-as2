from http import client
from urllib import response
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from course.views import index, course, detail, enroll, enrollresult, withdraw
from course.models import Course, Enroll
from django.contrib.auth.models import User

class TestUrls(SimpleTestCase):

    def test_index_url_resolved(self):
        url = reverse('course:index')
        self.assertEquals(resolve(url).func, index)

    def test_course_url_resolved(self):
        url = reverse('course:course')
        self.assertEquals(resolve(url).func, course)
    
    def test_detail_url_resolved(self):
        url = reverse('course:detail', args=[0])
        self.assertEquals(resolve(url).func, detail)

    def test_enroll_url_resolved(self):
        url = reverse('course:enroll', args=[0])
        self.assertEquals(resolve(url).func, enroll)
    
    def test_withdraw_url_resolved(self):
        url = reverse('course:withdraw', args=[0])
        self.assertEquals(resolve(url).func, withdraw)

    def test_enrollresult_url_resolved(self):
        url = reverse('course:enrollresult')
        self.assertEquals(resolve(url).func, enrollresult)

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.course = Course.objects.create(
            course='com',
            course_code='3',
            seat_quota=5,
            detail='good',
            semester='1',
            status=True)

        self.index_url = reverse('course:index')
        self.course_url = reverse('course:course')
        self.detail_url = reverse('course:detail', args=[self.course.id])
        self.enroll_url = reverse('course:enroll', args=[self.course.id])
        self.enrollresult_url = reverse('course:enrollresult')
        self.withdraw_url = reverse('course:withdraw', args=[self.course.id])

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

    def test_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'course/index.html')

    def test_course_GET(self):
        response = self.client.get(self.course_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'course/layout.html')

    def test_detail_GET(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'course/register.html')
    
    def test_enroll_GET(self):
        # get enroll
        self.client.login(username=self.username, password=self.password)

        response = self.client.get(self.enroll_url)

        self.assertEquals(response.status_code, 400)
        self.assertTemplateUsed(response, 'course/register.html')

    def test_enroll_POST(self):
        # enroll course that was enrolled
        self.client.login(username=self.username, password=self.password)

        Enroll.objects.create(
            user = self.user,
            course = self.course
        )

        response = self.client.post(self.enroll_url)

        self.assertEquals(response.status_code, 400)
        self.assertTemplateUsed(response, 'course/register.html')

    def test_enroll_POST_success(self):
        # enroll course success
        self.client.login(username=self.username, password=self.password)

        response = self.client.post(self.enroll_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'course/enrollresult.html')

    def test_enrollresult_GET(self):
        self.client.login(username=self.username, password=self.password)

        response = self.client.get(self.enrollresult_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'course/enrollresult.html')

    def test_withdraw_GET(self):
        # get withdraw
        self.client.login(username=self.username, password=self.password)

        response = self.client.get(self.withdraw_url)
        
        self.assertEquals(response.status_code, 400)
        self.assertTemplateUsed(response, 'course/index.html')

    def test_withdraw_POST(self):
        # post withdraw did not enroll
        self.client.login(username=self.username, password=self.password)

        response = self.client.post(self.withdraw_url)

        self.assertEquals(response.status_code, 400)
        self.assertTemplateUsed(response, 'course/register.html')

    def test_withdraw_POST_success(self):
        # post withdraw already enrolled
        self.client.login(username=self.username, password=self.password)

        Enroll.objects.create(
            user = self.user,
            course = self.course
        )

        response = self.client.post(self.withdraw_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'course/enrollresult.html')

    







