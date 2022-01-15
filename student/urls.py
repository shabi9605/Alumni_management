from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('student_register',views.student_register,name='student_register'),
    path('view_job_vacancy',views.view_job_vacancy,name='view_job_vacancy'),
    path('view_events',views.view_events,name='view_events'),
    path('apply_job/<int:id>',views.apply_job,name='apply_job'),
    path('view_my_job_application',views.view_my_job_application,name='view_my_job_application'),
    path('add_feedback',views.add_feedback,name='add_feedback'),
    path('view_feedbacks',views.view_feedbacks,name='view_feedbacks'),
    path('add_chat',views.add_chat,name='add_chat'),

    path('view_my_chat',views.view_my_chat,name='view_my_chat'),
    path('reply_chat/<int:id>',views.reply_chat,name='reply_chat'),

    path('student_profile_update',views.student_profile_update,name='student_profile_update'),

    


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)