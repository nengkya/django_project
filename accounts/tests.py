from django.test import TestCase
from django.contrib.auth import get_user_model

#create your tests here
class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username = 'micky', email = 'HaGa@haga.id', password = 'mouse')

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(username = 'superman', email = 'superman@comic.com', password = 'supergirl')
