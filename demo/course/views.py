from ast import And
from django.shortcuts import render
from django.contrib.auth.models import User
from course.models import Course, Enroll
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course
# Create your views here.
def index(request):
    courses = Course.objects.all()

    print(courses)
    return render(request, 'course/index.html', {
        'courses' : courses
    })
def course(request):
    return render(request, 'course/layout.html')

def detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, 'course/register.html', {
        'course': course
    })

def enroll(request):
    id = request.POST['courseID']
    user = User.objects.get(pk=request.user.id)
    course = Course.objects.get(pk = id)
    enroll = Enroll(user=user, course=course)
    enroll.save()
    courses = Course.objects.all()
    return HttpResponseRedirect(reverse('course:enrollresult'))

def enrollresult(request):
    enroll = Enroll.objects.filter(user_id = request.user.id).all()
    return render(request, 'course/enrollresult.html', {
        'enroll' : enroll
    })
#course_id = id, user_id = request.user.id
