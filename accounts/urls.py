from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup_brewer/', views.signup_brewer, name='signup_brewer'),
]
