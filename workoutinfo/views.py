from django.shortcuts import render, get_object_or_404
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


class MemberDetail(View):
    def get(self, request, pk):
        member = get_object_or_404(
            Member,
            pk=pk
        )
        membership_list = member.memberships.all()
        workoutplan_list = member.workoutplans.all()
        workout_list = member.workouts.all()
        nutritionplan_list = member.nutritionplans.all()
        return render(
            request,
            'workoutinfo/member_detail.html',
            {'member': member, 'workoutplan_list': workoutplan_list, 'membership_list': membership_list,
             'workout_list': workout_list, 'nutritionplan_list': nutritionplan_list}
        )


class TrainerList(View):
    def get(self, request):
        return render(
            request,
            'workoutinfo/trainer_list.html',
            {'trainer_list': Trainer.objects.all()}
        )


class TrainerDetail(View):
    def get(self, request, pk):
        trainer = get_object_or_404(
            Trainer,
            pk=pk
        )
        nutritionplan_list = trainer.nutritionplans.all()
        workout_list = trainer.workouts.all()
        return render(
            request,
            'workoutinfo/trainer_detail.html',
            {'trainer': trainer, 'workout_list': workout_list, 'nutritionplan_list': nutritionplan_list}
        )


class WorkoutPlanList(View):
    def get(self, request):
        return render(
            request,
            'workoutinfo/workoutplan_list.html',
            {'workoutplan_list': WorkoutPlan.objects.all()}
        )


class WorkoutPlanDetail(View):
    def get(self, request, pk):
        workoutplan = get_object_or_404(
            WorkoutPlan,
            pk=pk
        )
        member = workoutplan.member
        workout_list = workoutplan.workouts.all()
        return render(
            request,
            'workoutinfo/workoutplan_detail.html',
            {'workoutplan': workoutplan, 'workout_list': workout_list, 'member': member}
        )


class WorkoutList(View):
    def get(self, request):
        return render(
            request,
            'workoutinfo/workout_list.html',
            {'workout_list': Workout.objects.all()}
        )


class WorkoutDetail(View):
    def get(self, request, pk):
        workout = get_object_or_404(
            Workout,
            pk=pk
        )
        member = workout.member
        trainer = workout.trainer
        workoutplan = workout.workout_plan
        date = workout.date
        duration = workout.duration
        name = workout.name
        description = workout.description
        return render(
            request,
            'workoutinfo/workout_detail.html',
            {'workoutplan': workoutplan, 'trainer': trainer, 'member': member, 'date': date, 'duration': duration,
             'name': name,  'description': description}
        )


class NutritionPlanList(View):
    def get(self, request):
        return render(
            request,
            'workoutinfo/nutritionplan_list.html',
            {'nutritionplan_list': NutritionPlan.objects.all()}
        )


class NutritionPlanDetail(View):
    def get(self, request, pk):
        nutritionplan = get_object_or_404(
            NutritionPlan,
            pk=pk
        )
        return render(
            request,
            'workoutinfo/nutritionplan_detail.html',
            {'nutritionplan': nutritionplan}
        )


class MembershipList(View):
    def get(self, request):
        return render(
            request,
            'workoutinfo/membership_list.html',
            {'membership_list': Membership.objects.all()}
        )


class MembershipDetail(View):
    def get(self, request, pk):
        membership = get_object_or_404(
            Membership,
            pk=pk
        )
        member = membership.member
        payment_list = membership.payments.all()
        return render(
            request,
            'workoutinfo/membership_detail.html',
            {'membership': membership, 'member': member, 'payment_list': payment_list}
        )


class PaymentList(View):
    def get(self, request):
        return render(
            request,
            'workoutinfo/payment_list.html',
            {'payment_list': Payment.objects.all()}
        )


class PaymentDetail(View):
    def get(self, request, pk):
        payment = get_object_or_404(
            Payment,
            pk=pk
        )
        membership = payment.membership
        return render(
            request,
            'workoutinfo/payment_detail.html',
            {'membership': membership, 'payment': payment}
        )
