from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import University, User, Student, StudentDocument, AdmissionEvaluation


# Register your models here.

admin.site.register(User, UserAdmin)

admin.site.register(University)
admin.site.register(Student)
admin.site.register(StudentDocument)
admin.site.register(AdmissionEvaluation)