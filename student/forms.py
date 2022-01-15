from django import forms
from django.db.models import fields
from django.forms.fields import CharField
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StudentUserFrom(UserCreationForm):
    username=forms.CharField(help_text=None,label='Username')
    password1=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Password')
    password2=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Confirm Password')

    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2')
        labels=('password1','Password','password2','Confirm Password')


class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentRegister
        fields=('college_name','semester','course','batch','image','resume')



class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=('feedback',)


class ChatForm(forms.ModelForm):
    class Meta:
        model=Chat
        fields=('alumni','title','content')


class ChatReplyForm(forms.ModelForm):
    class Meta:
        model=Chat
        fields=('reply',)




class UserUpdate(forms.ModelForm):
     class Meta:
        model=User
        fields=('username','email')



class ProfileUpdate(forms.ModelForm):
    class Meta:
        model=StudentRegister
        fields=('college_name','semester','course','batch','image','resume')
