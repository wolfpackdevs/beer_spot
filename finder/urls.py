from django.urls import path
from . import views

urlpatterns = [
    path('dashbord/', views.dashbord, name='dashbord'),
    path('brewer/', views.brewer_dashbord, name='brewer'),
]