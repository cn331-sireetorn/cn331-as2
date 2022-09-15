from django.urls import path, include
from . import views

app_name = 'course'

urlpatterns = [
    path('', views.index, name='index'),
    path('course/', views.course, name='course'),
    path('detail/<int:course_id>', views.detail, name='detail'), 
    path('enroll', views.enroll, name='enroll'),
   
]