from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

import alumni

from . models import *
from . forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from student.models import *

# Create your views here.

def index(request):
    return render(request,'index.html')


def alumni_register(request):
    reg=False
    if request.method=="POST":
        user_form=UserFrom(data=request.POST)
        profile_form=ProfileForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            return redirect('user_login')
        else:
            return HttpResponse("Invalid Form")
    else:
        user_form=UserFrom()
        profile_form=ProfileForm()
    return render(request,'alumni_register.html',{'user_form':user_form,'profile_form':profile_form})



def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"YOUR PASSWORD SUCCESSFULLY UPDATED")
            return render(request,'change_password.html')
        else:
            messages.error(request,"PLEASE CORRECT ERROR")
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'change_password.html',{"form":form})



def update_profile(request):
    if request.method=="POST":
        update_form=UpdateForm(request.POST,instance=request.user)
        
        update_profile_form=UpdateProfileForm(request.POST,instance=request.user)
        #print(request.user.register)
        if update_form.is_valid() and update_profile_form.is_valid():
            update_form.save()
            update_profile_form.save()
            messages.success(request,f'Your Account has been Updated')
            return redirect('dashboard')
    else:
        update_form=UpdateForm(instance=request.user)
        update_profile_form=UpdateProfileForm(instance=request.user)
    context={
        'update_form':update_form,
        'update_profile_form':update_profile_form
    }
    return render(request,'update_profile.html',context)



def add_event(request):
    if request.method=="POST":
        event_form=EventForm(request.POST)
        if event_form.is_valid():
            cp=Event(user=request.user,event_name=event_form.cleaned_data['event_name'],event_date=event_form.cleaned_data['event_date'],event_area=event_form.cleaned_data['event_area'],event_time=event_form.cleaned_data['event_time'],description=event_form.cleaned_data['description'])
            cp.save()
            return render(request,'add_event.html',{'msg':'successfully added event'})
        else:
            return HttpResponse("Invalid form")
    event_form=EventForm()
    return render(request,'add_event.html',{'form':event_form})


def view_my_events(request):
    my_events=Event.objects.filter(user=request.user).order_by('-date')
    return render(request,'my_events.html',{'my_events':my_events})



def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        try:
            user1=AlumniRegister.objects.get(user=user)
        except:
            pass
        try:
            user2=StudentRegister.objects.get(user=user)
        except:
            pass

        if user:
            if user.is_active:
                try:
                    if user1:
                        active=AlumniRegister.objects.all().filter(user_id=user.id,status=True)
                        if active:
                            login(request,user)
                            return HttpResponseRedirect(reverse('dashboard'))
                        else:
                            return HttpResponse("Waiting for approval")
                except:
                    pass
                try:
                    if user2:
                        
                        login(request,user)
                        return HttpResponseRedirect(reverse('dashboard'))
                    else:
                        return HttpResponse("Waiting for approval")
                        
                except:
                    pass
                try:
                    if user.is_superuser:
                        
                        login(request,user)
                        return HttpResponseRedirect(reverse('dashboard'))
                    else:
                        return HttpResponse("Waiting for approval")
                        
                except:
                    pass
            else:
                return HttpResponse("Not active")
        else:
            return HttpResponse("Invalid username or password")
    else:
        
        return render(request,'login.html')






def dashboard(request):
    #list=Todo.objects.all()
    return render(request,'dashboard.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')



def add_companies(request):
    if request.method=="POST":
        company_form=AddCompanyForm(request.POST)
        if company_form.is_valid():
            cp=Company(comapany_name=company_form.cleaned_data['comapany_name'],company_area=company_form.cleaned_data['company_area'])
            cp.save()
            return render(request,'add_company.html',{'msg':'successfully added company'})
        else:
            return HttpResponse("Invalid form")
    company_form=AddCompanyForm()
    return render(request,'add_company.html',{'form':company_form})


def view_companies(request):
    companies=Company.objects.all()
    return render(request,'companies.html',{'companies':companies})



def add_job_vacancy(request):
    alumni=AlumniRegister.objects.get(user=request.user)
    print(alumni)
    if request.method=="POST":
        job_vacancy_form=JobVacancyForm(request.POST)
        if job_vacancy_form.is_valid():
            alumni=AlumniRegister.objects.get(user=request.user)
            print(alumni)
            cp=JobVacancies(user=request.user,alumni=alumni,company=job_vacancy_form.cleaned_data['company'],available_vacancy=job_vacancy_form.cleaned_data['available_vacancy'],job_type=job_vacancy_form.cleaned_data['job_type'],job_title=job_vacancy_form.cleaned_data['job_title'],description=job_vacancy_form.cleaned_data['description'])
            cp.save()
            return render(request,'add_vacancy.html',{'msg':'successfully added vaccancy'})
        else:
            return HttpResponse("Invalid form")
    job_vacancy_form=JobVacancyForm()
    return render(request,'add_vacancy.html',{'form':job_vacancy_form})


def view_vacancies(request):
    vacancies=JobVacancies.objects.filter().order_by('-date')
    return render(request,'my_vacancies.html',{'vacancies':vacancies})



def update_vacancy(request,id):
    Update = JobVacancies.objects.get(id=id)
    print(Update)
    form= JobVacancyForm(instance=Update)
    if request.method=='POST':
        form= JobVacancyForm(request.POST,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('dashboard')
    return render(request,'add_vacancy.html',{'form':form})



def delete_vacancy(request,id):
    Update = JobVacancies.objects.get(id=id)
    Update.delete()
    return redirect('dashboard')




def view_all_students(request):
    all_students=StudentRegister.objects.all().order_by('-id')
    return render(request,'view_students.html',{'all_students':all_students})



def view_all_alumni(request):
    all_alumni=AlumniRegister.objects.all().order_by('-id')
    return render(request,'view_alumni.html',{'all_alumni':all_alumni})


def view_all_companies(request):
    all_companies=Company.objects.all().order_by('-id')
    return render(request,'view_companies.html',{'all_companies':all_companies})




def delete_student(request,id):
    student=StudentRegister.objects.get(id=id)
    student.delete()
    return redirect('view_all_students')



def delete_alumni(request,id):
    student=AlumniRegister.objects.get(id=id)
    student.delete()
    return redirect('view_all_alumni')



def delete_company(request,id):
    student=Company.objects.get(id=id)
    student.delete()
    return redirect('view_all_companies')




def verify_alumni(request,id):
    Update = AlumniRegister.objects.get(id=id)
    print(Update)
    form= VerifyAlumni(instance=Update)
    if request.method=='POST':
        form= VerifyAlumni(request.POST,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('dashboard')
    return render(request,'verify_alumni.html',{'form':form})



def rating_form(request):
    if request.method=="POST":
        job_vacancy_form=RatingForm(request.POST)
        if job_vacancy_form.is_valid():
           
            cp=Rating(user=request.user,alumni=job_vacancy_form.cleaned_data['alumni'],rating=job_vacancy_form.cleaned_data['rating'])
            cp.save()
            return render(request,'add_rating.html',{'msg':'successfully added rating'})
        else:
            return HttpResponse("Invalid form")
    job_vacancy_form=RatingForm()
    return render(request,'add_rating.html',{'form':job_vacancy_form})
