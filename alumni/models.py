from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator

# Create your models here.
class AlumniRegister(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=PhoneNumberField()
    male='male'
    female='female'
    genders=[
        (male,'male'),
        (female,'female')

    ]
    gender=models.CharField(max_length=30,choices=genders,default=male)
    passout_batch=models.IntegerField()
    course_graduated=models.CharField(max_length=50)
    currently_connected_to=models.TextField()
    image=models.FileField(upload_to='images',null=True,blank=True)
    status=models.BooleanField(default=False)
    def __str__(self):
        return str(self.user.username)


class Company(models.Model):
    comapany_name=models.CharField(max_length=50)
    company_area=models.CharField(max_length=50)
    def __str__(self):
        return str(self.comapany_name)

class JobVacancies(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    alumni=models.ForeignKey(AlumniRegister,on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    available_vacancy=models.IntegerField()
    part_time='part_time'
    full_time='full_time'
    job_types=[
        (part_time,'part_time'),
        (full_time,'full_time')
    ]
    job_type=models.CharField(max_length=50,choices=job_types,default=full_time)
    job_title=models.CharField(max_length=50)
    description=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user.username)


class Event(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    event_name=models.CharField(max_length=50)
    event_date=models.DateField()
    event_area=models.CharField(max_length=50)
    event_time=models.CharField(max_length=30)
    description=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.event_name)




class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    alumni=models.ForeignKey(AlumniRegister,on_delete=models.CASCADE,null=True,blank=True)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    def __str__(self):
        return str(self.user.username)
