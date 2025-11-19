from mongoengine import Document, StringField, EmailField, ReferenceField, ListField, IntField, DateTimeField, FloatField, EmbeddedDocument, EmbeddedDocumentField
import datetime

class Team(Document):
    name = StringField(required=True, unique=True)
    members = ListField(EmailField())
    meta = {'collection': 'teams'}

class User(Document):
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    team = ReferenceField(Team, required=False)
    meta = {'collection': 'users'}

class Activity(Document):
    user = ReferenceField(User, required=True)
    type = StringField(required=True)
    duration = FloatField(required=True)  # minutes
    calories = IntField()
    date = DateTimeField(default=datetime.datetime.utcnow)
    meta = {'collection': 'activities'}

class Workout(Document):
    name = StringField(required=True)
    description = StringField()
    difficulty = StringField(choices=['easy', 'medium', 'hard'])
    meta = {'collection': 'workouts'}

class Leaderboard(Document):
    team = ReferenceField(Team, required=True)
    score = IntField(default=0)
    meta = {'collection': 'leaderboard'}
