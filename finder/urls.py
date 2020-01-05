from django.urls import path
from . import views

urlpatterns = [
    path('dashbord/', views.dashbord, name='dashbord'),
    path('brewer/', views.brewer_dashbord, name='brewer'),
    path('brewer/add/', views.add_beer, name='add_beer'),
    path('brewer/beers/', views.brewer_beer, name='brewers_beer'),
    path('brewer/beer/<int:id>/', views.beer_info, name='beer_info_1')
]