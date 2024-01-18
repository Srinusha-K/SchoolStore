from django.contrib import admin

# Register your models here.
from student_app.models import Courses, Department, St_data

admin.site.register(Courses)
admin.site.register(Department)
admin.site.register(St_data)