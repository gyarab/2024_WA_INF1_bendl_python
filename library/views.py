import os
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .models import Game # ,Comment
# from .forms import CommentForm
import json


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
