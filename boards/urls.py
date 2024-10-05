from django.urls import path 

from .views import IndexPageView, menuView, mostrar 

urlpatterns = [ 
    path('', IndexPageView.as_view(), name='index'), 
    path('menu/',  menuView, name='menu'), 
    path('listbook/',  mostrar, name='listbook'), ]