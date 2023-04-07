from django.contrib import admin
from .models import Member, Trainer, WorkoutPlan, Workout, NutritionPlan, Membership, Payment

# Register your models here.
admin.site.register(Member)
admin.site.register(Trainer)
admin.site.register(WorkoutPlan)
admin.site.register(Workout)
admin.site.register(NutritionPlan)
admin.site.register(Membership)
admin.site.register(Payment)


