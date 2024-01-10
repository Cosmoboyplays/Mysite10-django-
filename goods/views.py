from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404

from goods.models import Products


def catalog(request, category_slug):  # page=1
    page = request.GET.get('page', 1)

    if category_slug.lower() == 'all':
        goods = Products.objects.all()
    else:
        # ВАЖНО получение slug по внешнему ключу
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)  # int(page) без этого тоже робит пока

    context = {
        'title': 'Home - каталог',
        'goods': current_page,  # раньше тут была goods, до пагинации
        'slug_url': category_slug,
    }
    return render(request, 'goods/catalog.html', context)


def product(request, slug):
    product_ = Products.objects.get(slug=slug)
    context = {
        'product': product_
               }
    return render(request, 'goods/product.html', context)


