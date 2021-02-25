#import Http Response from django
from django.shortcuts import render
from .models import PostFeed
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.


journal = [
    {
        'user': 'Username',
        'title': 'title 1',
        'content': 'journal 1',
        'date_posted': 'January 5, 2021'
    },
    {
        'user': 'Username',
        'title': 'title 2',
        'content': 'journal 2',
        'date_posted': 'January 6, 2021' 
    },
    {
        'user': 'Username',
        'title': 'title 3',
        'content': 'journal 3',
        'date_posted': 'January 7, 2021'
    }
]


#create a function
def home_view(request):
    context = {
        'feed': PostFeed.objects.all()
    }
    # return response
    return render(request, "home.html", context)

def notepad_view(request):
    return render(request, "notepad.html")

def message_view(request):
    return render(request, "messages.html")

def journal_view(request):
    context = {
        'journal': journal
    }
    return render(request, "journal.html",context)

def notifications_view(request):
    return render(request, "notifications.html")

def settings_view(request):
    return render(request, "settings.html")