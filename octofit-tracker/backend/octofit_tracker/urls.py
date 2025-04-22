"""octofit_tracker URL Configuration

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
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/activities/", views.activities_list, name="activities_list"),
    path("api/workouts/", views.workouts_list, name="workouts_list"),
    path("api/leaderboard/", views.leaderboard_list, name="leaderboard_list"),
    path("api/teams/", views.teams_list, name="teams_list"),
    path("api/users/", views.users_list, name="users_list"),
]
