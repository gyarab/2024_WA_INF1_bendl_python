from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Game, Author, Genre, Comment
from .forms import CommentForm



def get_favorite_and_nonfavorite_games(gamesPool, user, excludeById=None):
    """
    tuple:
    - favorite_games = list of games favorited by the user from game pool
    - nonfavorite_games = list of games not favorited by the user / the whole pool if not authenticated.

    """
    if excludeById is not None:
        gamesPool = gamesPool.exclude(pk=excludeById)
    if user.is_authenticated:
        favorite_games = gamesPool.filter(favorited_by=user)
        nonfavorite_games = gamesPool.exclude(favorited_by=user)
    else:
        favorite_games = []
        nonfavorite_games = gamesPool
    return favorite_games, nonfavorite_games

def libraryHomepage(request):
    games = Game.objects.all()
    fav_games, nonfav_games = get_favorite_and_nonfavorite_games(games, request.user)

    return render(request, 'homepage.html', {
        'games': games,
        'favorite_games': fav_games,
        'nonfavorite_games': nonfav_games
    })

def gameInfo(request, id):
    games = Game.objects.all()
    game = get_object_or_404(Game, pk=id)
    fav_games, nonfav_games = get_favorite_and_nonfavorite_games(games, request.user, excludeById=game.pk)

    comments = game.comments.all().order_by('-created_at')

    form = CommentForm()

    if request.method == "POST" and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.game = game
            comment.ip_address = request.META.get('REMOTE_ADDR')
            comment.user_agent = request.META.get('HTTP_USER_AGENT')
            comment.save()
            return redirect('gameInfo', id=game.id)

    return render(request, 'game.html', {
        'game': game,
        'games': games,
        'comments': comments,
        'favorite_games': fav_games,
        'nonfavorite_games': nonfav_games,
        'form': form,
    })
def AuthorInfo(request, id):
    games = Game.objects.all()
    author = get_object_or_404(Author, pk=id)
    fav_games, nonfav_games = get_favorite_and_nonfavorite_games(Game.objects.filter(authors=author), request.user)

    return render(request, 'author.html', {
        'author': author,
        'games': games,
        'favorite_games': fav_games,
        'nonfavorite_games': nonfav_games,
    })

def GenreInfo(request, id):
    games = Game.objects.all()
    genre = get_object_or_404(Genre, pk=id)
    fav_games, nonfav_games = get_favorite_and_nonfavorite_games(Game.objects.filter(genres=genre), request.user)

    return render(request, 'genre.html', {
        'genre': genre,
        'games': games,
       'favorite_games': fav_games,
        'nonfavorite_games': nonfav_games,
    })

class LoginPageView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('libraryHomepage')
    
class RegisterPageView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('libraryHomepage')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPageView, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy('libraryHomepage'))
        return super(RegisterPageView, self).get(*args, **kwargs)

@require_POST
@login_required
def toggle_favorite(request):
    game_id = request.POST.get('game_id')
    print(f"Game ID: {game_id}")
    if not game_id:
        return JsonResponse({'error': 'No game ID provided.'}, status=400)

    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        return JsonResponse({'error': 'Game not found.'}, status=404)

    user = request.user
    if user in game.favorited_by.all():
        game.favorited_by.remove(user)
        favorited = False
    else:
        game.favorited_by.add(user)
        favorited = True

    return JsonResponse({'favorited': favorited})
