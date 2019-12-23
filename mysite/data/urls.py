from django.urls import path

from . import views

app_name = 'data'
urlpatterns = [
  path('', views.index, name='index'),
  path('nba/', views.nba, name='nba'),
  path('nba/players', views.nba_players, name='nba-players'),
  path('admin/nba/players/', views.admin_nba_players, name='admin-nba-players'),
  path('admin/nba/players/update/', views.admin_nba_players_update, name='admin-nba-players-update'),
]