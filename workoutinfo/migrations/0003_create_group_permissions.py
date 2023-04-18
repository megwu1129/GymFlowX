from __future__ import unicode_literals
from itertools import chain
from django.db import migrations


def populate_permissions_lists(apps):
    permission_class = apps.get_model('auth', 'Permission')

    member_permissions = permission_class.objects.filter(content_type__app_label='workoutinfo',
                                                             content_type__model='member')

    trainer_permissions = permission_class.objects.filter(content_type__app_label='workoutinfo',
                                                          content_type__model='trainer')

    workoutplan_permissions = permission_class.objects.filter(content_type__app_label='workoutinfo',
                                                                  content_type__model='workoutplan')

    workout_permissions = permission_class.objects.filter(content_type__app_label='workoutinfo',
                                                                  content_type__model='workout')

    nutritionplan_permissions = permission_class.objects.filter(content_type__app_label='workoutinfo',
                                                           content_type__model='nutritionplan')

    membership_permissions = permission_class.objects.filter(content_type__app_label='workoutinfo',
                                                         content_type__model='membership')

    payment_permissions = permission_class.objects.filter(content_type__app_label='workoutinfo',
                                                          content_type__model='payment')

    perm_view_member = permission_class.objects.filter(content_type__app_label='workoutinfo',
                                                           content_type__model='member',
                                                           codename='view_member')

    perm_view_trainer = permission_class.objects.filter(content_type__app_label='workoutinfo',
                                                        content_type__model='trainer',
                                                        codename='view_trainer')

    perm_view_workoutplan = permission_class.objects.filter(content_type__app_label='workoutinfo',
                                                               content_type__model='workoutplan',
                                                               codename='view_workoutplan')

    perm_view_workout = permission_class.objects.filter(content_type__app_label='workoutinfo',
                                                               content_type__model='workout',
                                                               codename='view_workout')

    perm_view_nutritionplan = permission_class.objects.filter(content_type__app_label='workoutinfo',
                                                         content_type__model='nutritionplan',
                                                         codename='view_nutritionplan')

    perm_view_membership = permission_class.objects.filter(content_type__app_label='workoutinfo',
                                                       content_type__model='membership',
                                                       codename='view_membership')

    perm_view_payment = permission_class.objects.filter(content_type__app_label='workoutinfo',
                                                        content_type__model='payment',
                                                        codename='view_payment')

    wi_user_permissions = chain(perm_view_member,
                                perm_view_trainer,
                                perm_view_workoutplan,
                                perm_view_workout,
                                perm_view_nutritionplan,
                                perm_view_membership,
                                perm_view_payment
                                )

    wi_admin_permissions = chain(member_permissions,
                                 trainer_permissions,
                                 workoutplan_permissions,
                                 workout_permissions,
                                 nutritionplan_permissions,
                                 membership_permissions,
                                 payment_permissions
                                 )

    wi_trainer_permissions = chain(workout_permissions,
                                   nutritionplan_permissions,
                                   workoutplan_permissions,
                                   perm_view_member,
                                   perm_view_trainer,
                                   perm_view_membership,
                                   perm_view_payment
                                   )

    my_groups_initialization_list = [
        {
            "name": "wi_user",
            "permissions_list": wi_user_permissions,
        },
        {
            "name": "wi_admin",
            "permissions_list": wi_admin_permissions,
        },
        {
            "name": "wi_trainer",
            "permissions_list": wi_trainer_permissions,
        },
    ]
    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)
    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)
    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):
    dependencies = [
        ('workoutinfo', '0002_create_groups'),
    ]

    operations = [
        migrations.RunPython(
            add_group_permissions_data,
            remove_group_permissions_data
        )
    ]
