"""
URL configuration for SplatourneySystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', views.player_registration, name='player_registration'),
    #path('register', views.register, name='register'),
    path('player_registration/', views.player_registration, name='player_registration'),
    path('', views.login_page, name='login_page'),
    path('tournament_details/', views.tournament_details, name='tournament_details'),
    path('team_registration/', views.team_registration, name='team_registration'),
    path('registrations/', views.view_registrations, name='view_registrations'),
    path('registration_type/', views.registration_type, name='registration_type'),
    path('login_page/', views.login_page, name='login_page'),
    path('login_moderator/', views.login_moderator, name='login_moderator'),
    path('create_tournament/', views.create_tournament, name='create_tournament'),
    path('edit_tournament/', views.edit_tournament, name='edit_tournament'),
    path('pairings/', views.pairings, name='pairings'),
    path('declare_winner/', views.declare_winner, name='declare_winner'),
    path('start_tournament/', views.start_tournament, name='start_tournament'),
    path('create_bracket/', views.create_bracket, name='create_bracketColumns'),
    path('create_team/', views.create_team, name='create_team'),
    path('create_tournament', views.create_tournament, name='create_tournament'),
    path('pairing_screens/', views.pairing_screens, name='pairing_screens'),
    path('tournaments_screen/', views.tournaments_screen, name='tournaments_screen'),
    path('edit_player_registration/', views.edit_player_registration, name='edit_player_registration'),
    path('edit_team_registration/', views.edit_team_registration, name='edit_team_registration'),
    path('create_moderator/', views.create_moderator, name='create_moderator'),
    path('manage_moderators/', views.manage_moderators, name='manage_moderators'),
]
