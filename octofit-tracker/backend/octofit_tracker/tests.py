from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='marvel')
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team, 'marvel')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='marvel', members=['test@example.com'])
        self.assertEqual(team.name, 'marvel')
        self.assertEqual(team.members, ['test@example.com'])

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user_email='test@example.com', activity='running', duration=30)
        self.assertEqual(activity.user_email, 'test@example.com')
        self.assertEqual(activity.activity, 'running')
        self.assertEqual(activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='marvel', points=100)
        self.assertEqual(leaderboard.team, 'marvel')
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(user_email='test@example.com', workout='pushups', reps=50)
        self.assertEqual(workout.user_email, 'test@example.com')
        self.assertEqual(workout.workout, 'pushups')
        self.assertEqual(workout.reps, 50)
