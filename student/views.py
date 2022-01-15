from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

from . models import *
from . forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from alumni.models import *

# Create your views here.

def student_register(request):
    reg=False
    if request.method=="POST":
        user_form=StudentUserFrom(data=request.POST)
        profile_form=StudentForm(data=request.POST)
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
        user_form=StudentUserFrom()
        profile_form=StudentForm()
    return render(request,'student_register.html',{'user_form':user_form,'profile_form':profile_form})


def view_job_vacancy(request):
    vacancies=JobVacancies.objects.all().order_by('-date')
    if request.method=="GET":
       
        name=request.GET.get('name')
        
        try:
            student=JobVacancies.objects.filter(title__icontains=name)
            print(student)
            return render(request,'vacancies.html',{'student':student})
        except:
            pass
    return render(request,'vacancies.html',{'vacancies':vacancies})

def view_events(request):
    events=Event.objects.all().order_by('-date')
    return render(request,'events.html',{'events':events})
    


def apply_job(request,id):
    student=StudentRegister.objects.get(user=request.user)
    vacancy=JobVacancies.objects.get(id=id)
    cp=ApplyJob(user=request.user,
    student=student,
    job=vacancy)
    cp.save()
    return redirect('view_job_vacancy')


def view_my_job_application(request):
    job_apply=ApplyJob.objects.filter(user=request.user)
    return render(request,'my_job_applications.html',{'job_apply':job_apply})



def add_feedback(request):
    if request.method=="POST":
        feedback_form=FeedbackForm(request.POST)
        if feedback_form.is_valid():
            cp=Feedback(user=request.user,feedback=feedback_form.cleaned_data['feedback'])
            cp.save()
            return render(request,'add_feedback.html',{'msg':'successfully added feedback'})
        else:
            return HttpResponse("Invalid form")
    feedback_form=FeedbackForm()
    return render(request,'add_feedback.html',{'form':feedback_form})



def view_feedbacks(request):
    my_feedback=Feedback.objects.filter(user=request.user).order_by('-id')
    all_feedback=Feedback.objects.all().order_by('-id')
    return render(request,'view_feedback.html',{'my_feedback':my_feedback,'all_feedback':all_feedback})




def add_chat(request):
    if request.method=="POST":
        chat_form=ChatForm(request.POST)
        if chat_form.is_valid():
            cp=Chat(user=request.user,alumni=chat_form.cleaned_data['alumni'],title=chat_form.cleaned_data['title'],content=chat_form.cleaned_data['content'])
            cp.save()
            return render(request,'add_chat.html',{'msg':'successfully added chat'})
        else:
            return HttpResponse("Invalid form")
    chat_form=ChatForm()
    return render(request,'add_chat.html',{'form':chat_form})



def view_my_chat(request):
    my_chat=Chat.objects.filter(user=request.user)
    try:
        received_chats=Chat.objects.filter(alumni=request.user.alumniregister)
        print(received_chats)
        return render(request,'view_chats.html',{'my_chat':my_chat,'received_chats':received_chats})
    except:
        return render(request,'view_chats.html',{'my_chat':my_chat})



def reply_chat(request,id):
    Update = Chat.objects.get(id=id)
    print(Update)
    form= ChatReplyForm(instance=Update)
    if request.method=='POST':
        form= ChatReplyForm(request.POST,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('dashboard')
    return render(request,'add_chat.html',{'form':form})







def student_profile_update(request):
    if request.method=="POST":
        update_form=UserUpdate(request.POST,instance=request.user)
        
        update_profile_form=ProfileUpdate(request.POST,instance=request.user)
        #print(request.user.register)
        if update_form.is_valid() and update_profile_form.is_valid():
            update_form.save()
            update_profile_form.save()
            messages.success(request,f'Your Account has been Updated')
            return redirect('dashboard')
    else:
        update_form=UserUpdate(instance=request.user)
        update_profile_form=ProfileUpdate(instance=request.user)
    context={
        'update_form':update_form,
        'update_profile_form':update_profile_form
    }
    return render(request,'update_profile.html',context)