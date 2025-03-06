# URLS pro aplikaci library
from django.urls import path
from . import views


urlpatterns = [
    path(''            , views.libraryHomepage),
    path('game/<int:id>', views.gameInfo)
     
]