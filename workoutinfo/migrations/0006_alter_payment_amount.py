# Generated by Django 4.1 on 2023-04-09 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workoutinfo", "0005_remove_payment_unique_payment_alter_workout_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="amount",
            field=models.DecimalField(
                decimal_places=2, help_text="Enter the amount in USD", max_digits=10
            ),
        ),
    ]