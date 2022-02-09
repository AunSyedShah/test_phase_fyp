from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Vehicle


# Create your views here.
def index(request):
    context = {}
    if request.method == "GET":
        return render(request, "add_vehicle.html")
    elif request.method == "POST":
        vehicle_number = request.POST["vehicle_number"]
        vehicle_brand = request.POST["vehicle_brand"]
        vehicle_model = request.POST["vehicle_model"]
        print(request.POST["add_search_radio"])
        vehicle_exists = Vehicle.objects.filter(vehicle_no=vehicle_number)
        if vehicle_exists:
            messages.error(request, "Vehicle Already Exists")
            return redirect("home")
        else:
            vehicle = Vehicle(vehicle_no=vehicle_number, brand=vehicle_brand, model=vehicle_model)
            vehicle.save()
            return redirect("home")


def search_vehicle(request):
    context = {

    }
    if request.method == "POST":
        vehicle_number = request.POST["vehicle_number_field"]
        vehicle_detail = Vehicle.objects.filter(vehicle_no=vehicle_number)
        if vehicle_detail:
            context["vehicle_detail"] = vehicle_detail
        else:
            messages.error(request, "No Vehicle Found")
        return render(request, "search_vehicle.html", context)
    return render(request, "search_vehicle.html")
