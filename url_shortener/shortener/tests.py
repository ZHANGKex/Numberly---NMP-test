from django.test import TestCase
from django.urls import reverse
from .models import URL

class URLShortenerTests(TestCase):

    def setUp(self):
        # Setup a test URL instance
        self.url = URL.objects.create(original_url="https://www.example.com", short_url="exmpl")

    def test_generate_short_url(self):
        # Test creating a short URL from a new original URL
        response = self.client.post(reverse('index'), {'original_url': 'https://www.newexample.com'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('short_url', response.context)  # Ensure the context contains 'short_url'
        new_url = URL.objects.get(original_url='https://www.newexample.com')
        self.assertIsNotNone(new_url)  # Ensure the new URL instance is created

    def test_redirect_to_original(self):
        # Test redirection from short URL to original URL
        response = self.client.get(reverse('redirect', args=['exmpl']))
        self.assertRedirects(response, "https://www.example.com", fetch_redirect_response=False)  # Ensure it redirects correctly

    def test_invalid_url(self):
        # Test handling of invalid URL input
        response = self.client.post(reverse('index'), {'original_url': 'invalid_url'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid URL format. Please enter a valid URL.')  # Ensure the error message is in the response

    def test_view_urls(self):
        # Test viewing all generated URLs
        response = self.client.get(reverse('view_urls'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'https://www.example.com')  # Ensure the original URL is in the response
        self.assertContains(response, 'http://localhost:8000/exmpl')  # Ensure the short URL is in the response
        
        # Ensure the number of URLs displayed matches the number of URLs in the database
        url_count = URL.objects.count()
        displayed_url_count = response.context['urls']
        self.assertEqual(len(displayed_url_count), url_count)  # Ensure the counts match


    def test_existing_url(self):
        # Test handling of existing original URL input
        response = self.client.post(reverse('index'), {'original_url': 'https://www.example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'http://localhost:8000/exmpl')  # Ensure the correct short URL is in the response

    def test_multiple_objects_returned(self):
        # Test handling of multiple URL entries for the same original URL
        URL.objects.create(original_url="https://www.duplicate.com", short_url="dup1")
        URL.objects.create(original_url="https://www.duplicate.com", short_url="dup2")
        response = self.client.post(reverse('index'), {'original_url': 'https://www.duplicate.com'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'http://localhost:8000/')  # Ensure the short URL is in the response

    def test_create_new_short_url(self):
        # Test creating a new short URL after deleting an existing one
        URL.objects.filter(original_url="https://www.newexample.com").delete()
        response = self.client.post(reverse('index'), {'original_url': 'https://www.newexample.com'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('short_url', response.context)  # Ensure the context contains 'short_url'
        new_url = URL.objects.get(original_url='https://www.newexample.com')
        self.assertIsNotNone(new_url)  # Ensure the new URL instance is created
        self.assertNotEqual(new_url.short_url, "exmpl")  # Ensure the short URL is not the same as 'exmpl'

    def test_can_get_into_index_page(self):
        # Test accessing the index page
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
