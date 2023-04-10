from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from workoutinfo.utils import ObjectCreateMixin
from workoutinfo.forms import MemberForm, TrainerForm, WorkoutPlanForm, WorkoutForm, NutritionPlanForm, MembershipForm, PaymentForm
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


class MemberCreate(ObjectCreateMixin, View):
    form_class = MemberForm
    template_name = 'workoutinfo/member_form.html'


class MemberUpdate(View):
    form_class = MemberForm
    model = Member
    template_name = 'workoutinfo/member_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        member = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=member),
            'member': member,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        member = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=member)
        if bound_form.is_valid():
            new_member = bound_form.save()
            return redirect(new_member)
        else:
            context = {
                'form': bound_form,
                'member': member,
            }
            return render(
                request,
                self.template_name,
                context)


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


class TrainerCreate(ObjectCreateMixin, View):
    form_class = TrainerForm
    template_name = 'workoutinfo/trainer_form.html'


class TrainerUpdate(View):
    form_class = TrainerForm
    model = Trainer
    template_name = 'workoutinfo/trainer_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        trainer = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=trainer),
            'trainer': trainer,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        trainer = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=trainer)
        if bound_form.is_valid():
            new_trainer = bound_form.save()
            return redirect(new_trainer)
        else:
            context = {
                'form': bound_form,
                'trainer': trainer,
            }
            return render(
                request,
                self.template_name,
                context)


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


class WorkoutPlanCreate(ObjectCreateMixin, View):
    form_class = WorkoutPlanForm
    template_name = 'workoutinfo/workoutplan_form.html'


class WorkoutPlanUpdate(View):
    form_class = WorkoutPlanForm
    model = WorkoutPlan
    template_name = 'workoutinfo/workoutplan_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        workoutplan = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=workoutplan),
            'workoutplan': workoutplan,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        workoutplan = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=workoutplan)
        if bound_form.is_valid():
            new_workoutplan = bound_form.save()
            return redirect(new_workoutplan)
        else:
            context = {
                'form': bound_form,
                'workoutplan': workoutplan,
            }
            return render(
                request,
                self.template_name,
                context)


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
        date = workout.date
        duration = workout.duration
        name = workout.name
        description = workout.description
        return render(
            request,
            'workoutinfo/workout_detail.html',
            {'workout': workout, 'trainer': trainer, 'member': member, 'date': date, 'duration': duration,
             'name': name,  'description': description}
        )


class WorkoutCreate(ObjectCreateMixin, View):
    form_class = WorkoutForm
    template_name = 'workoutinfo/workout_form.html'


class WorkoutUpdate(View):
    form_class = WorkoutForm
    model = Workout
    template_name = 'workoutinfo/workout_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        workout = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=workout),
            'workout': workout,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        workout = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=workout)
        if bound_form.is_valid():
            new_workout = bound_form.save()
            return redirect(new_workout)
        else:
            context = {
                'form': bound_form,
                'workout': workout,
            }
            return render(
                request,
                self.template_name,
                context)


class WorkoutDelete(View):
    def get(self, request, pk):
        workout = self.get_object(pk)
        return render(
            request,
            'workoutinfo/workout_confirm_delete.html',
            {'workout': workout}
        )

    def get_object(self, pk):
        workout = get_object_or_404(
            Workout,
            pk=pk)
        return workout

    def post(self, request, pk):
        workout = self.get_object(pk)
        workout.delete()
        return redirect('workoutinfo_workout_list_urlpattern')


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
        member = nutritionplan.member
        trainer = nutritionplan.trainer
        return render(
            request,
            'workoutinfo/nutritionplan_detail.html',
            {'nutritionplan': nutritionplan, 'member': member, 'trainer': trainer}
        )


class NutritionPlanCreate(ObjectCreateMixin, View):
    form_class = NutritionPlanForm
    template_name = 'workoutinfo/nutritionplan_form.html'


class NutritionPlanUpdate(View):
    form_class = NutritionPlanForm
    model = NutritionPlan
    template_name = 'workoutinfo/nutritionplan_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        nutritionplan = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=nutritionplan),
            'nutritionplan': nutritionplan,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        nutritionplan = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=nutritionplan)
        if bound_form.is_valid():
            new_nutritionplan = bound_form.save()
            return redirect(new_nutritionplan)
        else:
            context = {
                'form': bound_form,
                'nutritionplan': nutritionplan,
            }
            return render(
                request,
                self.template_name,
                context)


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


class MembershipCreate(ObjectCreateMixin, View):
    form_class = MembershipForm
    template_name = 'workoutinfo/membership_form.html'


class MembershipUpdate(View):
    form_class = MembershipForm
    model = Membership
    template_name = 'workoutinfo/membership_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        membership = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=membership),
            'membership': membership,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        membership = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=membership)
        if bound_form.is_valid():
            new_membership = bound_form.save()
            return redirect(new_membership)
        else:
            context = {
                'form': bound_form,
                'membership': membership,
            }
            return render(
                request,
                self.template_name,
                context)


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


class PaymentCreate(ObjectCreateMixin, View):
    form_class = PaymentForm
    template_name = 'workoutinfo/payment_form.html'


class PaymentUpdate(View):
    form_class = PaymentForm
    model = Payment
    template_name = 'workoutinfo/payment_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        payment = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=payment),
            'payment': payment,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        payment = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=payment)
        if bound_form.is_valid():
            new_payment = bound_form.save()
            return redirect(new_payment)
        else:
            context = {
                'form': bound_form,
                'payment': payment,
            }
            return render(
                request,
                self.template_name,
                context)
