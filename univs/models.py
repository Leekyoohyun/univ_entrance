from django.db import models

# Create your models here.

class University(models.Model):
    #id = 대학번호
    id = models.BigAutoField(primary_key=True)
    #name = 대학교 이름
    name = models.CharField(max_length=30)
    #address = 대학교 주소
    address = models.CharField(max_length=100, null=True)
    #address_detail = 상세주소
    address_detail = models.CharField(max_length=100, null=True)


class User(models.Model):
    #id = 면접관번호
    id = models.BigAutoField(primary_key=True)
    #password
    password = models.CharField(max_length = 50)
    #username = 닉네임
    username = models.CharField(max_length=150, unique=True)
    #대학번호
    university_id = models.ForeignKey('univs.University')