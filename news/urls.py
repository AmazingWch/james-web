from django.urls import path
from . import views


urlpatterns = [
    path('login', views.logIn),
    path('logout', views.logOut),
    path('poststory', views.postAStory),
    path('getstories', views.getStories),
    path('deletestory', views.deleteStory),
]



