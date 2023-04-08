from django.shortcuts import render
from django.views import View

from workoutinfo.models import Member, Trainer, WorkoutPlan, Workout, NutritionPlan, Membership, Payment
from django.views.generic import ListView


class MemberList(View):
    def get(self, request):
        return render(
            request,
            'workoutinfo/member_list.html',
            {'member_list': Member.objects.all()}
        )


class TrainerList(View):
    def get(self, request):
        return render(
            request,
            'workoutinfo/trainer_list.html',
            {'trainer_list': Trainer.objects.all()}
        )


class WorkoutPlanList(View):
    def get(self, request):
        return render(
            request,
            'workoutinfo/workoutplan_list.html',
            {'workoutplan_list': WorkoutPlan.objects.all()}
        )


class WorkoutList(View):
    def get(self, request):
        return render(
            request,
            'workoutinfo/workout_list.html',
            {'workout_list': Workout.objects.all()}
        )


class NutritionPlanList(View):
    def get(self, request):
        return render(
            request,
            'workoutinfo/nutritionplan_list.html',
            {'nutritionplan_list': NutritionPlan.objects.all()}
        )


class MembershipList(View):
    def get(self, request):
        return render(
            request,
            'workoutinfo/membership_list.html',
            {'membership_list': Membership.objects.all()}
        )


class PaymentList(View):
    def get(self, request):
        return render(
            request,
            'workoutinfo/payment_list.html',
            {'payment_list': Payment.objects.all()}
        )