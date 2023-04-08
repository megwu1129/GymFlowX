from django.shortcuts import render

from workoutinfo.models import Member, Trainer, WorkoutPlan, Workout, NutritionPlan, Membership, Payment


# Create your views here.
def member_list_view(request):
    member_list = Member.objects.all()
    # member_list = Member.objects.none()
    return render(request, 'workoutinfo/member_list.html', {'member_list': member_list})


def trainer_list_view(request):
    trainer_list = Trainer.objects.all()
    # trainer_list = Trainer.objects.none()
    return render(request, 'workoutinfo/trainer_list.html', {'trainer_list': trainer_list})


def workoutplan_list_view(request):
    workoutplan_list = WorkoutPlan.objects.all()
    # workoutplan_list = WorkoutPlan.objects.none()
    return render(request, 'workoutinfo/workoutplan_list.html', {'workoutplan_list': workoutplan_list})


def workout_list_view(request):
    workout_list = Workout.objects.all()
    # workout_list = Workout.objects.none()
    return render(request, 'workoutinfo/workout_list.html', {'workout_list': workout_list})


def nutritionplan_list_view(request):
    nutritionplan_list = NutritionPlan.objects.all()
    # nutritionplan_list = NutritionPlan.objects.none()
    return render(request, 'workoutinfo/nutritionplan_list.html', {'nutritionplan_list': nutritionplan_list})


def membership_list_view(request):
    membership_list = Membership.objects.all()
    # membership_list = Membership.objects.none()
    return render(request, 'workoutinfo/membership_list.html', {'membership_list': membership_list})


def payment_list_view(request):
    payment_list = Payment.objects.all()
    # payment_list = Payment.objects.none()
    return render(request, 'workoutinfo/payment_list.html', {'payment_list': payment_list})
