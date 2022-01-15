from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.index,name="index"),
    path('alumni_register',views.alumni_register,name="alumni_register"),
    path('dashboard',views.dashboard,name='dashboard'),
    path('user_login',views.user_login,name="user_login"),
    path('user_logout',views.user_logout,name="user_logout"),
    path('change_password',views.change_password,name='change_password'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('add_event',views.add_event,name='add_event'),
    path('view_my_events',views.view_my_events,name='view_my_events'),
    path('add_companies',views.add_companies,name='add_companies'),
    path('view_companies',views.view_companies,name='view_companies'),
    path('add_job_vacancy',views.add_job_vacancy,name='add_job_vacancy'),
    path('view_vacancies',views.view_vacancies,name='view_vacancies'),

    path('update_vacancy/<int:id>',views.update_vacancy,name='update_vacancy'),
    path('delete_vacancy/<int:id>',views.delete_vacancy,name='delete_vacancy'),


    path('view_all_students',views.view_all_students,name='view_all_students'),
    path('view_all_alumni',views.view_all_alumni,name='view_all_alumni'),
    path('view_all_companies',views.view_all_companies,name='view_all_companies'),

    path('delete_student/<int:id>',views.delete_student,name='delete_student'),
    path('delete_alumni/<int:id>',views.delete_alumni,name='delete_alumni'),
    path('delete_company/<int:id>',views.delete_company,name='delete_company'),

    path('verify_alumni/<int:id>',views.verify_alumni,name='verify_alumni'),

    path('rating_form',views.rating_form,name='rating_form'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)