from django.conf.urls import url
from .views import *
from game.models import *
from django.views.generic import ListView, DetailView

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r"^game/$", game, name="game"),
    url(r"^redir/$", redir, name="redirect"),
    url(r"^(?P<pk>\d+)$", test)
]
