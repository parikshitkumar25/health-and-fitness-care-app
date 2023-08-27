from django.forms import ModelForm
from django import forms
from .models import Exercise
from .models import Nutrition
from .models import  Settings
from .models import User
from django.forms import DateField,  ValidationError
import datetime
from .models import CustomPasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm



class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = [ 'date', 'exercise_type', 'duration', 'intensity' ]
        default_date = datetime.date.today()




class NutritionForm(ModelForm):
    class Meta:
        model = Nutrition
        fields = (
            'date',
            'meal_name',
            'calories',
            'fat',
            'protein',
            'carbs',
        )
  

class ProfileForm(ModelForm):
  class Meta:
    model = User
    fields = [
      'username',
      'email',
      'date_of_birth',
    ]
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['disabled'] = True
      
class SettingsForm(ModelForm):
  class Meta:
    model = Settings
    fields = [
    
       
      'notification_settings',
      'date_of_birth',
    ] 



class PasswordChangeCustomForm(PasswordChangeForm):
    pass

        
