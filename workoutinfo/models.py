from django.db import models
from django.core.validators import RegexValidator
from django.db.models import UniqueConstraint
from django.urls import reverse


# Create your models here.
class Member(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    member_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    disambiguator = models.CharField(max_length=45, blank=True, default='')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(
            r'^\+?\d{9,15}$',
            'Enter a valid phone number.'
        )]
    )

    def __str__(self):
        if self.disambiguator == '':
            return '%s, %s' % (self.last_name, self.first_name)
        else:
            result = '%s, %s (%s)' % (self.last_name, self.first_name, self.disambiguator)
        return result

    def get_absolute_url(self):
        return reverse('workoutinfo_member_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('workoutinfo_member_update_urlpattern',
                        kwargs={'pk': self.pk})

    class Meta:
        ordering = ['last_name', 'first_name', 'disambiguator']
        constraints = [
            models.UniqueConstraint(fields=['last_name', 'first_name', 'phone_number'], name='unique_member')
        ]


class Trainer(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    member_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    disambiguator = models.CharField(max_length=45, blank=True, default='')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(
            r'^\+?\d{9,15}$',
            'Enter a valid phone number.'
        )]
    )

    def __str__(self):
        if self.disambiguator == '':
            return '%s, %s' % (self.last_name, self.first_name)
        else:
            result = '%s, %s (%s)' % (self.last_name, self.first_name, self.disambiguator)
        return result

    def get_absolute_url(self):
        return reverse('workoutinfo_trainer_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('workoutinfo_trainer_update_urlpattern',
                        kwargs={'pk': self.pk})

    class Meta:
        ordering = ['last_name', 'first_name', 'disambiguator']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'phone_number'], name='unique_trainer')
        ]


class WorkoutPlan(models.Model):
    workout_plan_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    member = models.ForeignKey(Member, related_name='workoutplans', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.member} - {self.name}"

    def get_absolute_url(self):
        return reverse('workoutinfo_workoutplan_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('workoutinfo_workoutplan_update_urlpattern',
                        kwargs={'pk': self.pk})

    class Meta:
        ordering = ['member', 'name']
        constraints = [
            UniqueConstraint(fields=['name', 'member'], name='unique_workoutplan')
        ]


class Workout(models.Model):
    workout_id = models.AutoField(primary_key=True)
    date = models.DateField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField(help_text='Enter duration in minutes')
    workout_plan = models.ForeignKey(WorkoutPlan, related_name='workouts', on_delete=models.PROTECT)
    member = models.ForeignKey(Member, related_name='workouts', on_delete=models.PROTECT)
    trainer = models.ForeignKey(Trainer, related_name='workouts', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.member} - {self.name} / {self.date} / {self.trainer}"

    def get_absolute_url(self):
        return reverse('workoutinfo_workout_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    # def get_update_url(self):
    #     return reverse('workoutinfo_workout_update_urlpattern',
    #                     kwargs={'pk': self.pk})

    class Meta:
        ordering = ['member', 'name', 'date']
        constraints = [
            UniqueConstraint(fields=['member', 'name'], name='unique_workout')
        ]


class NutritionPlan(models.Model):
    TIME_CHOICES = [
        ('breakfast', 'BREAKFAST'),
        ('lunch', 'LUNCH'),
        ('dinner', 'DINNER'),
    ]
    nutrition_plan_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    member = models.ForeignKey(Member, related_name='nutritionplans', on_delete=models.PROTECT)
    trainer = models.ForeignKey(Trainer, related_name='nutritionplans', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.member} - {self.name} / {self.trainer}"

    def get_absolute_url(self):
        return reverse('workoutinfo_nutritionplan_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('workoutinfo_nutritionplan_update_urlpattern',
                        kwargs={'pk': self.pk})

    class Meta:
        ordering = ['member', 'name', 'trainer']
        constraints = [
            UniqueConstraint(fields=['member', 'name'], name='unique_nutritionplan')
        ]


class Membership(models.Model):
    membership_id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    member = models.ForeignKey(Member, related_name='memberships', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.member} / {self.start_date} ~ {self.end_date}"

    def get_absolute_url(self):
        return reverse('workoutinfo_membership_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('workoutinfo_membership_update_urlpattern',
                        kwargs={'pk': self.pk})

    class Meta:
        ordering = ['member', 'start_date', 'end_date']
        constraints = [
            UniqueConstraint(fields=['member', 'start_date', 'end_date'], name='unique_membership')
        ]


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('paypal', 'PayPal'),
        ('google_pay', 'Google Pay'),
        ('apple_pay', 'Apple Pay'),
        ('other', 'Other'),
    )
    payment_id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text='Enter the amount in USD')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_date = models.DateField(auto_now_add=True)
    membership = models.ForeignKey(Membership, related_name='payments', on_delete=models.PROTECT)
    member = models.ForeignKey(Member, related_name='payments', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.member} / {self.membership.start_date} ~ {self.membership.end_date}"
    
    def get_absolute_url(self):
        return reverse('workoutinfo_payment_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('workoutinfo_payment_update_urlpattern',
                        kwargs={'pk': self.pk})

    class Meta:
        ordering = ['member', 'payment_date']
