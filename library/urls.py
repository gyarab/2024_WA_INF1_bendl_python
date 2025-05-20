# URLS pro aplikaci library
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .views import LoginPageView, RegisterPageView

urlpatterns = [
    path('', views.libraryHomepage, name='libraryHomepage'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='libraryHomepage'), name='logout'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('game/<int:id>/', views.gameInfo, name='gameInfo'),
    path('toggle-favorite/', views.toggle_favorite, name='toggle_favorite'),

]