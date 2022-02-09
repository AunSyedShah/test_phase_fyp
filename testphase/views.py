from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Vehicle


# Create your views here.
def index(request):
    context = {}
    if request.method == "GET":
        return render(request, "add_vehicle.html")
    elif request.method == "POST":
        if "add_button" in request.POST:
            vehicle_number = request.POST["vehicle_number"]
            vehicle_brand = request.POST["vehicle_brand"]
            vehicle_model = request.POST["vehicle_model"]
            vehicle_exists = Vehicle.objects.filter(vehicle_no=vehicle_number)
            if vehicle_exists:
                messages.error(request, "Vehicle Already Exists")
                return redirect("home")
            else:
                vehicle = Vehicle(vehicle_no=vehicle_number, brand=vehicle_brand, model=vehicle_model)
                vehicle.save()
                return redirect("home")
        elif "search_button" in request.POST:
            vehicle_number = request.POST["vehicle_number_search"]
            vehicle_details = Vehicle.objects.filter(vehicle_no=vehicle_number)
            context["vehicle_details"] = vehicle_details
            return render(request, "add_vehicle.html", context)
