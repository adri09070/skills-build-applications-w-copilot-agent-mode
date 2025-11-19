from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from mongoengine import get_db

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear collections
        User.objects.delete()
        Team.objects.delete()
        Activity.objects.delete()
        Workout.objects.delete()
        Leaderboard.objects.delete()

        # Teams
        marvel = Team(name='Marvel', members=[]).save()
        dc = Team(name='DC', members=[]).save()

        # Users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel).save(),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel).save(),
            User(name='Captain America', email='cap@marvel.com', team=marvel).save(),
            User(name='Batman', email='batman@dc.com', team=dc).save(),
            User(name='Superman', email='superman@dc.com', team=dc).save(),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc).save(),
        ]
        marvel.members = [u.email for u in users if u.team.name == 'Marvel']
        dc.members = [u.email for u in users if u.team.name == 'DC']
        marvel.save()
        dc.save()

        # Workouts
        workouts = [
            Workout(name='Cardio Blast', description='Intense cardio session', difficulty='hard').save(),
            Workout(name='Strength Training', description='Build muscle', difficulty='medium').save(),
            Workout(name='Yoga Flow', description='Relax and stretch', difficulty='easy').save(),
        ]

        # Activities
        Activity(user=users[0], type='Running', duration=30, calories=300).save()
        Activity(user=users[1], type='Cycling', duration=45, calories=400).save()
        Activity(user=users[3], type='Swimming', duration=60, calories=500).save()
        Activity(user=users[4], type='Yoga', duration=40, calories=200).save()

        # Leaderboard
        Leaderboard(team=marvel, score=700).save()
        Leaderboard(team=dc, score=700).save()

        # Ensure unique index on email
        db = get_db()
        db.users.create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
