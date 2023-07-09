from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.home_page, name = 'home'),
    path('form/', views.form , name = 'form'),
    path('form1/' , views.form1 , name ="form1"),
]