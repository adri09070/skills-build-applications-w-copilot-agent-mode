from rest_framework import viewsets
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from octofit_tracker.serializers import (
    UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()

class WorkoutViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    queryset = Workout.objects.all()

class LeaderboardViewSet(viewsets.ModelViewSet):
    serializer_class = LeaderboardSerializer
    queryset = Leaderboard.objects.all()
