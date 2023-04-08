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
)

urlpatterns = [
    path('member/',
         MemberList.as_view(),
         name='workoutinfo_member_list_urlpattern'),
    path('trainer/',
         TrainerList.as_view(),
         name='workoutinfo_trainer_list_urlpattern'),
    path('workoutplan/',
         WorkoutPlanList.as_view(),
         name='workoutinfo_workoutplan_list_urlpattern'),
    path('workout/',
         WorkoutList.as_view(),
         name='workoutinfo_workout_list_urlpattern'),
    path('nutritionplan/',
         NutritionPlanList.as_view(),
         name='workoutinfo_nutritionplan_list_urlpattern'),
    path('membership/',
         MembershipList.as_view(),
         name='workoutinfo_membership_list_urlpattern'),
    path('payment/',
         PaymentList.as_view(),
         name='workoutinfo_payment_list_urlpattern'),
]