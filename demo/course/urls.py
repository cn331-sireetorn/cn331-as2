from django.urls import path, include
from . import views

app_name = 'course'

urlpatterns = [
    path('', views.index, name='index'),
    path('course/', views.course, name='course'),
    path('detail/<int:course_id>', views.detail, name='detail'), 
    path('enroll/<int:course_id>', views.enroll, name='enroll'),
    path('enrollresult',views.enrollresult,name='enrollresult'),
    path('withdraw/<int:course_id>', views.withdraw, name='withdraw')
]