"""jude_movieratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from movieratings.views import make_index, movie_view, user_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', make_index, name='index'),
    url(r'movie/(\d+$)', movie_view, name="selected_movie"),
    url(r'rater/(\d+)', user_view, name="user_page")


]
