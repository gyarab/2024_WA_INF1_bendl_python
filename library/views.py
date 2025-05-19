import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Game # ,Comment
# from .forms import CommentForm
import json


# Create your views here.
def libraryHomepage(request):
    games = Game.objects.all()
    return render(request, 'game_list.html', {'games': games})
#
def gameInfo(request, id):
    game = get_object_or_404(Game, pk=id)

    # comments = game.comments.all()
    # Form handling is commented out as requested
    # if request.method == "POST":
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.game = game
    #         comment.ip_address = request.META.get('REMOTE_ADDR')  # Get IP address
    #         comment.user_agent = request.META.get('HTTP_USER_AGENT')  # Get User Agent
    #         comment.save() 
    #         return redirect('gameInfo', id=game.id)
    # else:
    #     form = CommentForm()

    # Render the template without form-related context
    return render(request, 'game_detail.html', {
        'game': game,
        # 'comments': comments,
        # 'form': form  # Commented out as requested
    })
