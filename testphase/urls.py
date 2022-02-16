from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('deleteservice/<serviceid>', views.delete_service, name="delete_service"),
    path('addservice/<vehicle_number>', views.add_service, name="add_service"),
    path('updateservice/<service_id>', views.update_service, name="update_service"),
    path('search/', views.search_vehicle, name="search_vehicle"),
    path('delete/', views.delete_vehicle, name="delete_vehicle"),
]
