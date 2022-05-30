from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/get', views.api, name='api'),
]