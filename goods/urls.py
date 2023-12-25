from goods import views
from django.urls import path

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/', views.product, name='product')
    ]