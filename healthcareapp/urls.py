"""
URL configuration for healthcareapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  tracker import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registration/', views.registration_view, name='registartion' ),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('exercise_form/', views.add_exercise, name='exercise'),
    path('exercise_history/', views.exercise_history, name='exercise_history'),
    path('add_nutrition/' , views.add_nutrition, name='add_nutrition'),
    path('nutrition_history/', views.nutrition_history, name='nutrition_history'),
    path('create_goal/', views.create_goal, name='create_goal'),
    path('active_goal/', views.goals, name='active_goal'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
   
   
   # path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    #path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
  
]
