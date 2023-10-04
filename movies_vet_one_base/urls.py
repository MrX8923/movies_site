"""
URL configuration for movies_vet_one_base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from movies.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('django.contrib.auth.urls')),
    path('', index, name='home'),
    path('movies/', ListMovies.as_view(), name='all_movies'),
    # path('movie/<int:id>', info, name='info'),
    path('movie/<int:pk>/<str:title>', DetailMovie.as_view(), name='info'),
    path('actors/', ListActors.as_view(), name='all_actors'),
    path('actor/<int:pk>/<str:actor>', DetailActor.as_view(), name='info_actor'),
    path('subscription/', subscription, name='subscription'),
    path('subsription/see/<int:id1>/<int:id2>/<int:id3>', see_movie, name='see_movie')
]
