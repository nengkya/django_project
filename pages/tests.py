from django.test import SimpleTestCase
from django.urls import reverse

#create your tests here
class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_homepage_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'home page') 

    def test_homepage_does_not_contain_incorrect_html(self):
        response = self.client.get('')
        self.assertNotContains(response, 'fuck you')
        #self.assertNotContains(response, 'home page') fail
