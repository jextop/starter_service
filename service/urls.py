from django.urls import path

from . import views

urlpatterns = [
    path('', views.chk, name='chk'),
    path('chk', views.chk, name='chk'),
]
