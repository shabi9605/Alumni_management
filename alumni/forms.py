from django import forms
from django.forms.fields import CharField
from django.forms.widgets import SelectDateWidget
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserFrom(UserCreationForm):
    username=forms.CharField(help_text=None,label='Username')
    password1=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Password')
    password2=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Confirm Password')

    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')
        labels=('password1','Password','password2','Confirm Password')


class ProfileForm(forms.ModelForm):
    class Meta:
        model=AlumniRegister
        fields=('phone','gender','passout_batch','course_graduated','currently_connected_to','image')



class UpdateForm(forms.ModelForm):
    username=forms.CharField(help_text=None,label='Username')
    
    class Meta:
        model=User
        fields=('username','email')

class UpdateProfileForm(forms.ModelForm):
    address=forms.Textarea()
    
    class Meta:
        model=AlumniRegister
        fields='__all__'


class AddCompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields=('comapany_name','company_area')

class JobVacancyForm(forms.ModelForm):
    description=forms.Textarea()
    part_time='part_time'
    full_time='full_time'
    job_types=[
        (part_time,'part_time'),
        (full_time,'full_time')
    ]
    job_type=forms.ChoiceField(required=True,choices=job_types)
    class Meta:
        model=JobVacancies
        fields=('company','available_vacancy','job_type','job_title','description')


class EventForm(forms.ModelForm):
    description=forms.Textarea()
    event_date=forms.DateField(label='Event Date',widget=SelectDateWidget)
    
    class Meta:
        model=Event
        fields=('event_name','event_date','event_area','event_time','description')




class VerifyAlumni(forms.ModelForm):
    class Meta:
        model=AlumniRegister
        fields=('status',)

    

class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        fields=('alumni','rating')