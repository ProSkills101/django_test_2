from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

import requests
from bs4 import BeautifulSoup
from datetime import date

from .models import NBA_Player

# Create your views here.
def index(request):
  return render(request, 'data/index.html')

def nba(request):
  return render(request, 'data/nba.html')

def nba_players(request):
  players = NBA_Player.objects.all()
  context = {'players': players}
  return render(request, 'data/nba_players.html', context)

def admin_nba_players(request):
  if request.user.is_superuser:
    players = NBA_Player.objects.all()
    context = {'players': players}
    return render(request, 'data/admin_nba_players.html', context)
  
  return HttpResponse('Unauthorized', status=401)

def _validate_player(player):
  errors = {}
  if not player.get('stats_player_id'):
    errors['stats_player_id'] = { 'msg': 'stats_player_id can not be blank.' }
  if not player.get('name'):
    errors['name'] = { 'msg': 'name can not be blank.' }
  return errors

def admin_nba_players_update(request):
  if request.user.is_superuser:
    if request.method == 'POST':
      stats_player_id = request.POST.get('stats_player_id')

      page = requests.get('https://stats.nba.com/player/' + str(stats_player_id) + '/')
      soup = BeautifulSoup(page.content, 'html.parser')
      el_player = soup.find('div', { 'class': 'player-summary' })
      first_name = el_player.find('p', { 'class': 'player-summary__first-name'}).text
      last_name = el_player.find('p', { 'class': 'player-summary__last-name'}).text
      name = '{} {}'.format(first_name, last_name)

      text = el_player.find('span', { 'class': 'player-summary__player-number'}).text
      number = int(text[1:])
      
      team = el_player.find('span', { 'class': 'player-summary__team-name'}).text
      
      stats_item = el_player.find('div', { 'class': 'player-stats__height'})
      text = stats_item.find('span', { 'class': 'player-stats__stat-value'}).text
      tokens = text.split('-')
      ht = (float(tokens[0]) * 12 + float(tokens[1])) * 2.54
      
      stats_item = el_player.find('div', { 'class': 'player-stats__weight'})
      text = stats_item.find('span', { 'class': 'player-stats__stat-value'}).text
      tokens = text.split()
      wt = float(tokens[0])
      
      stats_item = el_player.find('div', { 'class': 'player-stats__birthdate'})
      text = stats_item.find('span', { 'class': 'player-stats__stat-value'}).text
      tokens = text.split('/')
      born = date(int(tokens[2]), int(tokens[0]), int(tokens[1]))

      stats_item = el_player.find('div', { 'class': 'player-stats__prior'})
      prior = stats_item.find('span', { 'class': 'player-stats__stat-value'}).text

      stats_item = el_player.find('div', { 'class': 'player-stats__draft'})
      draft = stats_item.find('span', { 'class': 'player-stats__stat-value'}).text

      stats_item = el_player.find('div', { 'class': 'player-stats__experience'})
      text = stats_item.find('div', { 'class': 'player-stats__stat-value'}).text
      tokens = text.split()
      exp = float(tokens[0])

      stats_item = el_player.find('div', { 'class': 'player-stats__pts'})
      text = stats_item.find('span', { 'class': 'player-stats__stat-value'}).text
      pts = float(text)

      stats_item = el_player.find('div', { 'class': 'player-stats__reb'})
      text = stats_item.find('span', { 'class': 'player-stats__stat-value'}).text
      reb = float(text)

      stats_item = el_player.find('div', { 'class': 'player-stats__ast'})
      text = stats_item.find('span', { 'class': 'player-stats__stat-value'}).text
      ast = float(text)

      stats_item = el_player.find('div', { 'class': 'player-stats__pie'})
      text = stats_item.find('span', { 'class': 'player-stats__stat-value'}).text
      pie = float(text)
      
      '''
      print("---------------------------------------")
      print(first_name)
      print(last_name)
      print(number)
      print(team)
      print(ht)
      print(wt)
      print(born)
      print(prior)
      print(draft)
      print(exp)
      print(pts)
      print(reb)
      print(ast)
      print(pie)
      '''

      players = NBA_Player.objects.filter(stats_player_id=stats_player_id)
      player = None if len(players) == 0 else players[0]

      if not player:
        errors = _validate_player({
          'stats_player_id': stats_player_id,
          'name': name, 
        })
        if errors:
          return JsonResponse({ 'errors': errors })
        
        player = NBA_Player(name=name, stats_player_id=stats_player_id, number=number, 
          team=team, ht=ht, wt=wt, born=born, prior=prior, draft=draft, exp=exp, 
          pts=pts, reb=reb, ast=ast, pie=pie)
        player.save()
        
        return JsonResponse({ 'status': 200, 'msg': 'success' })

      else:
        errors = _validate_player({
          'stats_player_id': stats_player_id,
          'name': name, 
        })
        if errors:
          return JsonResponse({ 'errors': errors })

        player.name = name
        player.stats_player_id = stats_player_id 
        player.number = number
        player.team=team
        player.ht=ht
        player.wt=wt 
        player.born=born
        player.prior=prior 
        player.draft=draft
        player.xp=exp
        player.pts=pts 
        player.reb=reb 
        player.ast=ast 
        player.pie=pie
        player.save()
        
        return JsonResponse({ 'status': 200, 'msg': 'success' })

  return JsonResponse({ 'status': 401, 'msg': 'unauthorized' })
