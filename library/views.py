import os
from django.shortcuts import render
from django.http import HttpResponse
from .models import Game
import json


# Create your views here.
def libraryHomepage(request):
    games = Game.objects.all()
    return render(request, 'game_list.html', {'games': games})

def gameInfo(request, id):
    game = Game.objects.get(pk=id)
    return render(request, 'game_detail.html', {'game': game})



    # with open(os.path.join(os.path.dirname(__file__), 'games.json'), encoding='utf-8') as f:
    #     games = json.load(f)
    # gamesImg = ""
    # for index, game in enumerate(games):
    #     gamesImg += f'<a href="./game/{index}"><img src="{game["image"]}" alt="{game["name"]}"></a>'
    # return HttpResponse(gamesImg)

# def gameInfo(request, id):
#     with open(os.path.join(os.path.dirname(__file__), 'games.json'), encoding='utf-8') as f:
#         games = json.load(f)
#     gamesInfo = games[int(id)]
#     name  = gamesInfo["name"]
#     desc  = gamesInfo["description"]
#     image = gamesInfo["image"]
#     genre = gamesInfo["genre"]
#     autor = gamesInfo["autor"]
#     return HttpResponse(f"""
#         <h1>{name}</h1>
#         <p>{desc}</p>
#         <img src="{image}" alt="{name}">
#         <p>Žánr:  {genre} </p>
#         <p>Autor: {autor} </p>
#     """)