from django.contrib import admin
from .models import Exercise , Nutrition, Goal

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass

# Register your models here.

@admin.register(Nutrition)
class NutritionAdmin(admin.ModelAdmin):
    list_display = (
        'meal_name',
        'calories',
        'fat',
        'protein',
        'carbs',
        'user',
    )

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = (
        
    )
