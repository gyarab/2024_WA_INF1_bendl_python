import os
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Game
from django.views.decorators.csrf import csrf_exempt


def gameInfo(request, id):
    game = get_object_or_404(Game, pk=id)
    all_games = Game.objects.all()

    return render(request, 'game.html', {
        'game': game,
        'games' : all_games
        })

def libraryHomepage(request):

    all_games = Game.objects.all().prefetch_related('favorited_by') 

    for game in all_games:
        game.is_favorited = request.user.is_authenticated and request.user in game.favorited_by.all()

    return render(request, 'homepage.html', {
        'games':  all_games
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

from django.conf import settings
from django.utils.text import get_valid_filename
from uuid import uuid4
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import os

@csrf_protect  # Enables CSRF protection
@login_required
def model_upload(request):
    if request.method == 'POST' and request.FILES.get('model_file'):
        model_file = request.FILES['model_file']

        # Validate file size and extension
        if model_file.size > 10 * 1024 * 1024:
            return JsonResponse({'error': 'File too large.'}, status=400)

        allowed_extensions = ['.glb', '.gltf']
        if not any(model_file.name.endswith(ext) for ext in allowed_extensions):
            return JsonResponse({'error': 'Unsupported file type.'}, status=400)

        # Safe filename handling
        filename = get_valid_filename(model_file.name)
        filename = f"{uuid4().hex}_{filename}"
        file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', filename)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb+') as destination:
            for chunk in model_file.chunks():
                destination.write(chunk)

        return JsonResponse({'status': 'success', 'file': filename})

    return JsonResponse({'error': 'No file uploaded.'}, status=400)
