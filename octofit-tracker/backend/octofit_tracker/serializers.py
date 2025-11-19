from rest_framework import serializers
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class TeamSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    members = serializers.ListField(child=serializers.EmailField())

class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    email = serializers.EmailField()
    team = serializers.CharField(allow_null=True)

class ActivitySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField()
    type = serializers.CharField()
    duration = serializers.FloatField()
    calories = serializers.IntegerField()
    date = serializers.DateTimeField()

class WorkoutSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    difficulty = serializers.CharField()

class LeaderboardSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    team = serializers.CharField()
    score = serializers.IntegerField()
