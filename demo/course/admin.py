from django.contrib import admin
from .models import Course, Enroll
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['course', 'course_code', 'seat_quota', 'detail', 'semester', 'status']

class EnrollAdmin(admin.ModelAdmin):
    list_display = ['user', 'course']

admin.site.register(Course, CourseAdmin)
admin.site.register(Enroll)