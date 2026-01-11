from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),

    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('alumni/', views.alumni_list, name='alumni_list'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/add/', views.add_job, name='add_job'),
]
