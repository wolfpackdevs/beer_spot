from django.urls import path
from . import views

urlpatterns = [
    path('dashbord/', views.dashbord, name='dashbord'),
    path('tutorial/', views.tutorial_1, name='tutorial_1'),
    path('tutorial/<int:id>', views.tutorial_2, name='tutorial_2'),
    path('beers/', views.all_beers, name='all_beers'),
    path('beers/<int:id>', views.beer_f_info, name='beer_f_info'),
    path('beers/like/<int:id>', views.like_beer, name='like'),
    path('beers/dislike/<int:id>', views.dislike_beer, name='dislike'),
]