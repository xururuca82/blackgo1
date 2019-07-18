from django.shortcuts import render
from django.views.generic.list import ListView

from .models import *


def index(request):
    return render(request, 'blackgo/index.html')


class BlackgoCafeListView(ListView):
    model = BlackgoCafe


class BlackgoUnivEntranceListView(ListView):
    model = BlackgoUnivEntrance


class BlackgoAcademyList(ListView):
    model = BlackgoOnlineAcademy