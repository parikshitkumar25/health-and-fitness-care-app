from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Exercise, Nutrition, Goal
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import SettingsForm, ProfileForm, ExerciseForm
from django.views.generic import TemplateView
from .forms import PasswordChangeCustomForm 
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages



def home(request):
    return render(request, 'home.html')

def registration(request):
    return render(request, 'registration.html')

def logoutpage(request):
  logout(request)
  return render(request, 'home.html')



def login_view(request):
    from django.contrib.auth.models import User
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate (request, username=username, password=password)
        if user is not None:
            login(request, user)
            return  redirect('home') 
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')






def registration_view(request):
    from django.contrib.auth.models import User
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create a new User object and save it to the database
        user = User.objects.create_user(
             username=username,
            email=email,
            password=password
        )
        
        if user is not None:
            authenticated_user = authenticate(username=username, email=email)
        if authenticated_user is not None:
              authenticated_user.set_password(password)
              authenticated_user.save()
            
        return redirect('login')
    else:
            return render(request, 'registration.html', {
                'error': 'Invalid username, email or password.'
            })
    

            # Optionally, you can log in the user after registration.
                #auth.login(request, user)

        #return redirect('home.html')  # Redirect to the login page after successful registration

    #return render(request, 'registration.html')


def add_exercise(request):
    from django.contrib.auth.models import User
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exercise_history')  # Redirect to the exercise history page
    else:
        form = ExerciseForm()
    
    return render(request, 'exercise_form.html', {'form': form})

def exercise_history(request):
    exercises = Exercise.objects.all()  # Fetch all exercise records from the database
    context = {'exercises': exercises}
    return render(request, 'exercise_history.html', context)

def add_nutrition(request):
    if request.method == 'POST':
        meal_name = request.POST.get('meal_name==0')
        if not meal_name:
         meal_name = "Unknown"
        calories = request.POST.get('calories')
        fat = request.POST.get('fat')
        protein = request.POST.get('protein')
        carbs = request.POST.get('carbs')

        new_nutrition = Nutrition(
            meal_name=meal_name,
            calories=calories,
            fat=fat,
            protein=protein,
            carbs=carbs,
            user=request.user,
        )
         # Check if meal_name is empty
        #if not meal_name:
         #meal_name = "Unknown"

        new_nutrition.save()
        print(new_nutrition)

        return redirect('nutrition_history')

    else:
        return render(request, 'nutrition_form.html')


        """"
        if meal_name is None or meal_name == "":
            meal_name = "Unknown"
        else:
            meal_name = meal_name
        """
        """""
        if meal_name is None:
            meal_name = "Unknown"
        elif len(meal_name) == '':
            meal_name = "Unknown"
        else:
            meal_name = meal_name
         """   
        #if len(meal_name) == 0 or meal_name is None:
         #   meal_name = "Unknown"


        #if meal_name is None or not isinstance(meal_name, str):
         #   meal_name = "Unknown"
        #if meal_name is None or len(meal_name) == 0:
         #   meal_name = "Unknown"
        
        #if meal_name is None:
         #   meal_name = "Unknown"
        #elif len(meal_name) == 0:
         #   meal_name = "Unknown"
        
        #if not meal_name:
            #meal_name = "Unknown"


"""""
def add_nutrition(request):
    form = NutritionForm(request.POST)

    if form.is_valid():
        nutrition = form.save(commit=False)
        nutrition.user = request.user
        nutrition.save()

        return redirect('nutrition_history')

    else:
        return render(request, 'nutrition_form.html', {'form': form})
"""

def nutrition_history(request):
    if request.user.is_authenticated:
        nutrition_list = Nutrition.objects.filter(user=request.user)
        meal_names = [nutrition.meal_name for nutrition in nutrition_list]
        if meal_names:
            most_common_meal_name = max(set(meal_names), key=meal_names.count)
        else:
            most_common_meal_name = None

        total_calories = sum([nutrition.calories for nutrition in nutrition_list])
        total_fat = sum([nutrition.fat for nutrition in nutrition_list])
        total_protein = sum([nutrition.protein for nutrition in nutrition_list])
        total_carbs = sum([nutrition.carbs for nutrition in nutrition_list])
        
        nutrition_statistics = {
            'total_calories': total_calories,
            'total_fat': total_fat,
            'total_protein': total_protein,
            'total_carbs': total_carbs,
            
        }

        return render(request, 'nutrition_history.html', {
            'nutrition_list': nutrition_list,
            'nutrition_statistics': nutrition_statistics,
        })

    else:
        return redirect('home')



@login_required
def create_goal(request):
  if request.method == 'POST':
    goal_type = request.POST.get('goal_type')
    target_date = request.POST.get('target_date')
    specific_objectives = request.POST.get('specific_objectives')

    goal = Goal(
      goal_type=goal_type,
      target_date=target_date,
      specific_objectives=specific_objectives,
      user=request.user,
    )
    goal.save()

    return redirect('active_goal')

  return render(request,'create_goal.html')

def goals(request):
  active_goals = Goal.objects.filter(user=request.user, is_active=True)

  return render(request, 'active_goals.html', {
    'active_goals': active_goals,
  })



@login_required
def profile(request):
    user = request.user
    form = ProfileForm(instance=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {
        'form': form,
    }

    return render(request, 'profile.html', context)



@login_required
def settings(request):
    user = request.user

    form = SettingsForm(instance=user.settings)

    if request.method == 'POST':
        form = SettingsForm(request.POST, instance=user.settings)
        if form.is_valid():
            form.save()
            return redirect('settings')

    context = {
        'form': form,
    }

    return render(request, 'settings.html', context)


"""
def settings(request):
    user = request.user

    context = {
        'user': user,
    }

    return render(request, 'settings.html', context)
    """

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeCustomForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeCustomForm(request.user)
    return render(request, 'change_password.html', {'form': form})