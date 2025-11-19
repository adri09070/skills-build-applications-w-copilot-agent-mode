from rest_framework.test import APITestCase
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class UserApiTest(APITestCase):
    def test_list_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

class TeamApiTest(APITestCase):
    def test_list_teams(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)

class ActivityApiTest(APITestCase):
    def test_list_activities(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, 200)

class WorkoutApiTest(APITestCase):
    def test_list_workouts(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, 200)

class LeaderboardApiTest(APITestCase):
    def test_list_leaderboard(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, 200)
