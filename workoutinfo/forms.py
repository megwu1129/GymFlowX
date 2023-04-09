from django import forms

from workoutinfo.models import Member, Trainer, WorkoutPlan, Workout, NutritionPlan, Membership, Payment


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator'].strip()
        return result

    def clean_gender(self):
        return self.cleaned_data['gender'].strip()

    def clean_phone_number(self):
        return self.cleaned_data['phone_number'].strip()


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip().capitalize()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip().capitalize()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator'].strip().capitalize()
        return result

    def clean_gender(self):
        return self.cleaned_data['gender'].strip()

    def clean_phone_number(self):
        return self.cleaned_data['phone_number'].strip()


class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }

    field_order = ['member', 'start_date', 'end_date', 'name', 'description']

    def clean_name(self):
        return self.cleaned_data['name'].strip().capitalize()

    def clean_description(self):
        return self.cleaned_data['description'].strip().capitalize()


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = '__all__'

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    field_order = ['member', 'trainer', 'workout_plan', 'date', 'name', 'description', 'duration']

    def clean_name(self):
        return self.cleaned_data['name'].strip().capitalize()

    def clean_description(self):
        return self.cleaned_data['description'].strip().capitalize()


class NutritionPlanForm(forms.ModelForm):
    class Meta:
        model = NutritionPlan
        fields = '__all__'

    field_order = ['member', 'trainer', 'name', 'meal_timing', 'description']

    def clean_name(self):
        return self.cleaned_data['name'].strip().capitalize()

    def clean_description(self):
        return self.cleaned_data['description'].strip().capitalize()

    def clean_meal_timing(self):
        return self.cleaned_data['meal_timing'].strip().capitalize()


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }

    field_order = ['member', 'start_date', 'end_date']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

        widgets = {
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
        }

    field_order = ['member', 'membership', 'payment_date', 'payment_method', 'amount']



