from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout
from django.http import JsonResponse

@api_view(['GET'])
def api_root(request, format=None):
    base_url = 'https://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev/'
    return Response({
        'users': base_url + 'api/users/?format=api',
        'teams': base_url + 'api/teams/?format=api',
        'activities': base_url + 'api/activities/?format=api',
        'leaderboard': base_url + 'api/leaderboard/?format=api',
        'workouts': base_url + 'api/workouts/?format=api'
    })

def activities_list(request):
    # Example data for activities
    activities = [
        {"id": 1, "name": "Running", "calories_burned": 300},
        {"id": 2, "name": "Cycling", "calories_burned": 250},
        {"id": 3, "name": "Swimming", "calories_burned": 400},
    ]
    return JsonResponse(activities, safe=False)

@api_view(['GET'])
def workouts_list(request):
    # Example data for workouts
    workouts = [
        {"id": 1, "name": "Morning Yoga", "duration": 30, "calories_burned": 200},
        {"id": 2, "name": "HIIT Session", "duration": 45, "calories_burned": 500},
        {"id": 3, "name": "Evening Run", "duration": 60, "calories_burned": 400},
    ]
    return JsonResponse(workouts, safe=False)

@api_view(['GET'])
def leaderboard_list(request):
    # Example data for leaderboard
    leaderboard = [
        {"id": 1, "name": "Alice", "score": 1500},
        {"id": 2, "name": "Bob", "score": 1200},
        {"id": 3, "name": "Charlie", "score": 1000},
    ]
    return JsonResponse(leaderboard, safe=False)

@api_view(['GET'])
def teams_list(request):
    # Example data for teams
    teams = [
        {"id": 1, "name": "Team Alpha", "members": 5},
        {"id": 2, "name": "Team Beta", "members": 8},
        {"id": 3, "name": "Team Gamma", "members": 3},
    ]
    return JsonResponse(teams, safe=False)

@api_view(['GET'])
def users_list(request):
    # Example data for users
    users = [
        {"id": 1, "username": "john_doe", "email": "john@example.com"},
        {"id": 2, "username": "jane_doe", "email": "jane@example.com"},
        {"id": 3, "username": "sam_smith", "email": "sam@example.com"},
    ]
    return JsonResponse(users, safe=False)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer