from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('accedi', views.accedi, name = 'accedi'),
    path('registrati', views.registrati, name = 'registrati'),
]