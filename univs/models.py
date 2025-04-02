from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.

class University(models.Model):
    #id = 대학번호
    id = models.IntegerField(primary_key=True)
    #name = 대학교 이름
    name = models.CharField(max_length=30)
    #address = 대학교 주소
    address = models.CharField(max_length=100, null=True)
    #address_detail = 상세주소
    address_detail = models.CharField(max_length=100, null=True)


class User(AbstractUser):
    #id = 면접관번호
    id = models.IntegerField(primary_key=True)
    # #password
    password = models.CharField(max_length = 50)
    #username = 닉네임
    username = models.CharField(max_length=150, unique=True)
    #대학번호
    university_id = models.ForeignKey('univs.University', on_delete=models.CASCADE, null = True)

class AdmissionEvaluation(models.Model):
    #id = 고유번호
    #자동생성?
    id = models.IntegerField(primary_key=True)
    #comment = 총평
    comment = models.TextField()
    
    #score = 점수
    score = models.IntegerField(null=True)
    
    #admission_type=지원유형
    class AdmissionType(models.TextChoices):
        # ("DB에 저장될 내용", "django 관리자 페이지 등등에서 보여질 내용")
        RECORDS = ("학생부종합", "학생부 종합입니다.")
        SUBJECT = ("학생부교과", "학생부 교과입니다.")

    admission_type = models.CharField(max_length = 10, choices=AdmissionType.choices)

    #user_id
    user_id = models.ForeignKey('univs.User', on_delete=models.CASCADE)
    
    #student_id
    student_id = models.ForeignKey('univs.Student', on_delete=models.CASCADE)


class Student(models.Model):
    id = models.CharField(max_length=8 ,primary_key=True)

    name = models.CharField(max_length=10)
    birth = models.DateField()

    class GenderType(models.TextChoices):
        MALE = ("남", "남자입니다.")
        FEMALE = ("여", "여자입니다.")

    gender = models.CharField(max_length=1, choices=GenderType.choices)

    memo = models.CharField(max_length=500, null=True)


class StudentDocument(models.Model):
    id = models.IntegerField(primary_key=True)
    file = models.FileField(max_length=255, upload_to='\media', null=True)#파일위치 어디로할지 모르겠음
    date = models.DateField(auto_now_add=True)
    student_id = models.ForeignKey('univs.Student', on_delete=models.CASCADE)