from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup_brewer/', views.signup_brewer, name='signup_brewer'),
    path('edit_brewery/', views.edit_brewery, name='edit_brewery'),
    path('edit_brewer/', views.edit_brewer, name='edit_brewer'),
    path('change_password/', views.change_password, name='change_password'),
    path('edit_profile/', views.edit_viewer, name='edit_viewer'),
    path('edit_pic/', views.change_viewer_pic, name='edit_pic')
]
