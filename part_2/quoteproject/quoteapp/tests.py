# quoteproject/tests.py
import os
from django.test import TestCase
from django.contrib.auth.models import User
from quoteproject.quoteapp.models import Author, Quote

os.environ['DJANGO_SETTINGS_MODULE'] = 'quoteproject.project_settings.settings'
settings.configure()

class QuoteAppTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create test data
        self.author = Author.objects.create(name='Test Author', bio='Test Bio')
        self.quote = Quote.objects.create(text='Test Quote', author=self.author)

    def test_author_str(self):
        self.assertEqual(str(self.author), 'Test Author')

    def test_quote_str(self):
        self.assertEqual(str(self.quote), 'Test Quote - Test Author')

    def test_register_view(self):
        response = self.client.post('/quoteproject/quoteapp/templates/registration/register/', {'username': 'newuser',
                                                   'password1': 'newpassword', 'password2': 'newpassword'})
        self.assertEqual(response.status_code, 302)  # 302 is the HTTP status code for a successful redirect

    def test_login_view(self):
        response = self.client.post('/quoteproject/quoteapp/templates/registration/login/', {'username': 'testuser',
                                                                                     'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)

    def test_author_list_view(self):
        response = self.client.get('/quoteproject/quoteapp/templates/author_quote/author_list/')  # Modify the path based on your structure
        self.assertEqual(response.status_code, 200)  # Assuming the view returns a 200 status for a successful request

    def test_quote_list_view(self):
        response = self.client.get('/quoteproject/quoteapp/templates/author_quote/quote_list/')  # Modify the path based on your structure
        self.assertEqual(response.status_code, 200)

    def test_add_author_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post('/quoteproject/quoteapp/templates/author_quote/add_author/', {'name': 'New Author', 'bio': 'New Bio'})
        self.assertEqual(response.status_code, 302)

    def test_add_quote_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post('/quoteproject/quoteapp/templates/author_quote/add_quote/', {'text': 'New Quote', 'author': self.author.id})
        self.assertEqual(response.status_code, 302)
