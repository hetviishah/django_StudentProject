from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Batch)
admin.site.register(Subjects)