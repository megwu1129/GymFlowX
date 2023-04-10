"""fitness_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from workoutinfo.views import (
    MemberList,
    TrainerList,
    WorkoutPlanList,
    WorkoutList,
    NutritionPlanList,
    MembershipList,
    PaymentList,
    MemberDetail,
    TrainerDetail,
    NutritionPlanDetail,
    WorkoutPlanDetail,
    WorkoutDetail,
    MembershipDetail,
    PaymentDetail,
    MemberCreate,
    TrainerCreate,
    WorkoutPlanCreate,
    WorkoutCreate,
    NutritionPlanCreate,
    MembershipCreate,
    PaymentCreate,
    MemberUpdate,
    TrainerUpdate,
    WorkoutPlanUpdate,
    WorkoutUpdate,
    NutritionPlanUpdate,
)



urlpatterns = [
    path('member/',
         MemberList.as_view(),
         name='workoutinfo_member_list_urlpattern'),

    path('member/<int:pk>/',
         MemberDetail.as_view(),
         name='workoutinfo_member_detail_urlpattern'),

    path('member/create/',
         MemberCreate.as_view(),
         name='workoutinfo_member_create_urlpattern'),

    path('member/<int:pk>/update/',
         MemberUpdate.as_view(),
         name='workoutinfo_member_update_urlpattern'),

    path('trainer/',
         TrainerList.as_view(),
         name='workoutinfo_trainer_list_urlpattern'),

    path('trainer/<int:pk>/',
         TrainerDetail.as_view(),
         name='workoutinfo_trainer_detail_urlpattern'),

    path('trainer/create/',
         TrainerCreate.as_view(),
         name='workoutinfo_trainer_create_urlpattern'),

    path('trainer/<int:pk>/update/',
         TrainerUpdate.as_view(),
         name='workoutinfo_trainer_update_urlpattern'),

    path('workoutplan/',
         WorkoutPlanList.as_view(),
         name='workoutinfo_workoutplan_list_urlpattern'),

    path('workoutplan/<int:pk>/',
         WorkoutPlanDetail.as_view(),
         name='workoutinfo_workoutplan_detail_urlpattern'),

    path('workoutplan/create/',
         WorkoutPlanCreate.as_view(),
         name='workoutinfo_workoutplan_create_urlpattern'),

    path('workoutplan/<int:pk>/update/',
         WorkoutPlanUpdate.as_view(),
         name='workoutinfo_workoutplan_update_urlpattern'),

    path('workout/',
         WorkoutList.as_view(),
         name='workoutinfo_workout_list_urlpattern'),

    path('workout/<int:pk>/',
         WorkoutDetail.as_view(),
         name='workoutinfo_workout_detail_urlpattern'),

    path('workout/create/',
         WorkoutCreate.as_view(),
         name='workoutinfo_workout_create_urlpattern'),

    path('workout/<int:pk>/update/',
         WorkoutUpdate.as_view(),
         name='workoutinfo_workout_update_urlpattern'),

    path('nutritionplan/',
         NutritionPlanList.as_view(),
         name='workoutinfo_nutritionplan_list_urlpattern'),

    path('nutritionplan/<int:pk>/',
         NutritionPlanDetail.as_view(),
         name='workoutinfo_nutritionplan_detail_urlpattern'),

    path('nutritionplan/create/',
         NutritionPlanCreate.as_view(),
         name='workoutinfo_nutritionplan_create_urlpattern'),

    path('nutritionplan/<int:pk>/update/',
         NutritionPlanUpdate.as_view(),
         name='workoutinfo_nutritionplan_update_urlpattern'),

    path('membership/',
         MembershipList.as_view(),
         name='workoutinfo_membership_list_urlpattern'),

    path('membership/<int:pk>/',
         MembershipDetail.as_view(),
         name='workoutinfo_membership_detail_urlpattern'),

    path('membership/create/',
         MembershipCreate.as_view(),
         name='workoutinfo_membership_create_urlpattern'),

    path('payment/',
         PaymentList.as_view(),
         name='workoutinfo_payment_list_urlpattern'),

    path('payment/<int:pk>/',
         PaymentDetail.as_view(),
         name='workoutinfo_payment_detail_urlpattern'),

    path('payment/create/',
         PaymentCreate.as_view(),
         name='workoutinfo_payment_create_urlpattern'),
]

