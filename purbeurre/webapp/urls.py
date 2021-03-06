""" URL Configuration for web app """

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('selection', views.selection, name='selection'),
    path('result', views.result, name='result'),
    path('save', views.save, name='save'),
    path("myfood", views.myfood, name='myfood'),
    path('del_sub', views.del_sub, name='del_sub'),
]
