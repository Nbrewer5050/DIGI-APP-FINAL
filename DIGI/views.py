#import Http Response from django
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from .models import PostFeed


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

class PostListView(ListView):
    model = PostFeed
    template_name = 'home.html'
    context_object_name = 'post'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = PostFeed



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