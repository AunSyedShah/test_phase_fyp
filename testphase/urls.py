from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('deleteservice/<serviceid>', views.delete_service, name="delete_service"),
]
