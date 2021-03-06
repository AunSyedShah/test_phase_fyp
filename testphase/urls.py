from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('search/', views.search_vehicle, name="search_vehicle"),
    path('delete/', views.delete_vehicle, name="delete_vehicle"),
    path('update/', views.update_vehicle, name="update_vehicle"),
    path('add/', views.add_vehicle, name="add_vehicle"),
    path('add-service/', views.add_service_detail, name="add_service_detail"),
    path('get-services/', views.get_vehicle_details, name="get-services"),
    path('delete-service/<service_id>', views.delete_vehicle_details, name="delete-service"),
    path('update-service/', views.update_vehicle_detail, name="update-service"),
]
