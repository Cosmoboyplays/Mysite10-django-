from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {'title': 'home',
               'content': 'Магазин мебели HOME',
               'list': ['1', 1, [2]],
               'dict': {3: 4},
               'bool': False}
    return render(request, 'hub/index.html', context)


def about(request):
    context = dict(title='О нас', content='О нас',
                   text_on_page="Много много много текста о нас, какие мы крутые, что нас отличает,"
                                "какие мы все тут особенные и классные")
    return render(request, 'hub/about.html', context)
