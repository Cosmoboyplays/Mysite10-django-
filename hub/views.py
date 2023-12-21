from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {'title': 'home',
               'content': 'Главная страничка моего сайта',
               'list': ['1', 1, [2]],
               'dict': {3: 4},
               'bool': False}
    return render(request, 'hub/index.html', context)


def about(request):
    return HttpResponse("About page")
