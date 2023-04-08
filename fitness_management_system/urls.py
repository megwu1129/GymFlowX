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
from django.contrib import admin
from django.urls import path
from workoutinfo.views import (
    member_list_view,
    trainer_list_view,
    workoutplan_list_view,
    workout_list_view,
    nutritionplan_list_view,
    membership_list_view,
    payment_list_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/', member_list_view),
    path('trainer/', trainer_list_view),
    path('workoutplan/', workoutplan_list_view),
    path('workout/', workout_list_view),
    path('nutritionplan/', nutritionplan_list_view),
    path('membership/', membership_list_view),
    path('payment/', payment_list_view)
]
