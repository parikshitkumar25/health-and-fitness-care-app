from wsgiref.validate import validator
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import datetime
from django.core.validators import MaxValueValidator
from django.utils import timezone
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy





# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    from django.db import models



class Exercise(models.Model):
    EXERCISE_TYPES = [
        ('Running', 'Running'),
        ('Cycling', 'Cycling'),
        ('Swimming', 'Swimming'),
        # Add more exercise types as needed
    ]

    date = models.DateField(default=datetime.date.today())  # Date of the exercise
    exercise_type = models.CharField(max_length=100, choices=EXERCISE_TYPES)
    duration = models.PositiveIntegerField()  # In minutes
    intensity = models.PositiveIntegerField()  # On a scale of 1 to 10

    def __str__(self):
        return f" Date: {self.date},{self.exercise_type} - Duration: {self.duration} mins, Intensity: {self.intensity}/10"




class Nutrition(models.Model):
    date = models.DateField(default=datetime.date.today())
    meal_name = models.CharField(max_length=255)
    calories = models.IntegerField()
    fat = models.IntegerField()
    protein = models.IntegerField()
    carbs = models.IntegerField()
    user = models.ForeignKey(
        to='auth.User',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.meal_name



from django.db import models

class Goal(models.Model):
  goal_type = models.CharField(max_length=255)
  target_date = models.DateField()
  specific_objectives = models.TextField()
  user = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE,
  )
  is_active = models.BooleanField(default=True)

  def __str__(self):
    return self.goal_type



class User(models.Model):
  username = models.CharField(max_length=100, unique=True) 
  email = models.EmailField(max_length=255)
  password_confirm = models.CharField(max_length=128, null=True, default='')
  date_of_birth = models.DateField(blank=True, null=True)

  password = models.CharField(max_length=128, null=True)
  notification_settings = models.BooleanField(default=True)

class Settings(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  date_of_birth = models.DateField()
  notification_settings = models.BooleanField(default=True)
  

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('password_change_done')