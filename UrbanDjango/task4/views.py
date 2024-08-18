from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


def platform(request):
    return render(request, 'fourth_task/platform.html')


def games(request):
    context = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay2"]}
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    return render(request, 'fourth_task/cart.html')
