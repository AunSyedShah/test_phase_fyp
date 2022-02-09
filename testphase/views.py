from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import VehicleForm
from .models import Vehicle


# Create your views here.
def index(request):
    context = {}
    if request.method == "GET":
        vehicle_form = VehicleForm()
        context["vehicle_form"] = vehicle_form
        return render(request, "add_vehicle.html", context)
    elif request.method == "POST":
        vehicle_form = VehicleForm(request.POST)
        if vehicle_form.is_valid():
            vehicle_form.save()
            messages.success(request, "Vehicle Added")
            return redirect("home")
        else:
            messages.error(request, "Vehicle Number already exists")
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
