from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from alumni.models import *

# Create your models here.
class StudentRegister(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    college_name=models.CharField(max_length=50)
    semester=models.IntegerField(null=True,blank=True)
    course=models.CharField(max_length=50,null=True,blank=True)
    batch=models.CharField(max_length=50,null=True,blank=True)
    image=models.FileField(upload_to='iamge',null=True,blank=True)
    resume=models.FileField(upload_to='resume',null=True,blank=True)
    def __str__(self):
        return str(self.user.username)




class ApplyJob(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    job=models.ForeignKey(JobVacancies,on_delete=models.CASCADE,null=True,blank=True)
    student=models.ForeignKey(StudentRegister,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return str(self.user.username)




class Feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    feedback=models.TextField()
    date=DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user.username)



class Chat(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    alumni=models.ForeignKey(AlumniRegister,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=50)
    content=models.TextField()
    reply=models.TextField(null=True,blank=True)
    date=DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user.username)

    