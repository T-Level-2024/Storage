# Import tools we need
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from django.conf import settings
from django.core.wsgi import get_wsgi_application
import os
from pymongo import MongoClient
from datetime import datetime

# Tell Django where to find our template
settings.configure(
    DEBUG=True,
    SECRET_KEY=get_random_secret_key(),
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ),
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__), 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        }
    }]
)

# Connect to MongoDB
client = MongoClient('mongodb+srv://30178812:Database%20Password@cluster0.i56il.mongodb.net/')
db = client['school_database']
collection = db['student_preferences']

# Handle our web pages
def form_view(request):
    # If someone submits the form:
    if request.method == 'POST':
        # Get the data they entered
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        likes_mango = request.POST.get('likes_mango') == 'yes'

        # Save it to MongoDB
        collection.insert_one({
            'name': name,
            'dob': datetime.strptime(dob, '%Y-%m-%d'),
            'likes_mango': likes_mango
        })

        return HttpResponse('Thanks for telling us about your mango preference! 🥭')

    # If someone just visits the page:
    return render(request, 'form.html')

# Tell Django which URLs to use
urlpatterns = [
    path('', form_view, name='form'),
]

# Start the website
application = get_wsgi_application()

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'runserver', '8000'])
