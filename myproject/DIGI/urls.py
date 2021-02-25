from django.urls import path
from . import views
from .views import home_view, notepad_view, message_view, journal_view, notifications_view, settings_view



urlpatterns = [
    path('DIGI', home_view, name='home'),
    path('notepad/', notepad_view, name='notepad'),
    path('messages/', message_view, name="messages"),
    path('journal./', journal_view, name="journal"),
    path('notifications', notifications_view, name="notifications"),
    path('settings', settings_view, name="settings"),
    
]