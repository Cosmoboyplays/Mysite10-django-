from goods import views
from django.urls import path

app_name = 'goods'

urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('<slug:category_slug>/<int:page>', views.catalog, name='index'),
    path('product/<slug:slug>/', views.product, name='product')
    ]