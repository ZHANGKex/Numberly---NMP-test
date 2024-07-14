from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import validators
from .models import URL
import string
import random

def generate_unique_short_url():
    """
    Generate a unique short URL consisting of 6 random characters.
    This function ensures the generated short URL is not already in the database.
    """
    while True:
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        if not URL.objects.filter(short_url=short_url).exists():
            return short_url

def index(request):
    """
    Handle the index page which contains the form to shorten URLs.
    If the request method is POST, validate the input URL and either retrieve
    or create a new shortened URL. Return the shortened URL to the user.
    """
    if request.method == 'POST':
        original_url = request.POST['original_url']
        
        if not validators.url(original_url):
            return render(request, 'index.html', {'error': 'Invalid URL format. Please enter a valid URL.'})
        
        try:
            url_instance = URL.objects.get(original_url=original_url)
        except URL.DoesNotExist:
            short_url = generate_unique_short_url()
            url_instance = URL.objects.create(original_url=original_url, short_url=short_url)
        except URL.MultipleObjectsReturned:
            url_instance = URL.objects.filter(original_url=original_url).first()

        full_short_url = f'http://localhost:8000/{url_instance.short_url}'
        return render(request, 'result.html', {'short_url': full_short_url})
    
    return render(request, 'index.html')


def redirect_to_original(request, short_url):
    """
    Handle redirection from a short URL to the original URL.
    If the short URL exists, redirect to the original URL. Otherwise, return a 404 error.
    """
    url = get_object_or_404(URL, short_url=short_url)
    return redirect(url.original_url)

def view_urls(request):
    """
    Display a list of all generated URLs.
    """
    urls = URL.objects.all()
    full_urls = [{'original_url': url.original_url, 'short_url': f'http://localhost:8000/{url.short_url}'} for url in urls]
    return render(request, 'view_urls.html', {'urls': full_urls})