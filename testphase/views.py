from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Vehicle, Services


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
            # if fields are empty
            if vehicle_number == "" or vehicle_brand == "" or vehicle_model == "":
                messages.error(request, "Fields can not be empty")
                return redirect("home")
            # if vehicle are already exists
            vehicle_exists = Vehicle.objects.filter(vehicle_no=vehicle_number)
            if vehicle_exists:
                messages.error(request, "Vehicle Already Exists")
                return redirect("home")
            else:
                vehicle = Vehicle(vehicle_no=vehicle_number, brand=vehicle_brand, model=vehicle_model)
                vehicle.save()
                messages.error(request, "Record Saved Successfully")
                return redirect("home")
        elif "search_button" in request.POST:
            vehicle_number = request.POST["vehicle_number"]
            if vehicle_number == "":
                messages.error(request, "Vehicle Number field can not be empty")
                return redirect("home")
            vehicle_details = Vehicle.objects.filter(vehicle_no=vehicle_number)
            if not vehicle_details:
                messages.error(request, "no vehicle found with the provided Vehicle Number")
                return redirect("home")
            context["vehicle_details"] = vehicle_details
            services_details = Services.objects.filter(vehicle_no=vehicle_number)
            context["services_details"] = services_details
            return render(request, "add_vehicle.html", context)
        elif "update_button" in request.POST:
            vehicle_number = request.POST["vehicle_number"]
            vehicle_brand = request.POST["vehicle_brand"]
            vehicle_model = request.POST["vehicle_model"]
            vehicle_object_update = Vehicle.objects.get(vehicle_no=vehicle_number)
            vehicle_object_update.brand = vehicle_brand
            vehicle_object_update.model = vehicle_model
            vehicle_object_update.save()
            messages.success(request, "record updated successfully")
            return redirect("home")
        elif "delete_button" in request.POST:
            vehicle_number = request.POST["vehicle_number"]
            Vehicle.objects.get(vehicle_no=vehicle_number).delete()
            messages.success(request, "record deleted successfully")
            return redirect("home")


def delete_service(request, serviceid):
    Services.objects.get(serviceID=serviceid).delete()
    return redirect("home")


def add_service(request, vehicle_number):
    if request.method == "POST":
        vehicle_object = Vehicle.objects.get(vehicle_no=vehicle_number)
        service_id = request.POST["service_id"]
        service_type = request.POST["service_type"]
        service_object = Services.objects.filter(serviceID=service_id)
        if service_object:
            messages.error(request, "service id is already associated with this or some other vehicle")
            return HttpResponseRedirect(request.path_info)
        service_object = Services(serviceID=service_id, type=service_type, vehicle_no=vehicle_object)
        service_object.save()
        messages.success(request, f"service: {service_type} with service ID {service_id} created successfully")
        return HttpResponseRedirect(request.path_info)
    return render(request, "add_service_detail.html")


def update_service(request, service_id):
    context = {

    }
    if request.method == "POST":
        service_type = request.POST["service_type"]
        service_object = Services.objects.get(serviceID=service_id)
        service_object.type = service_type
        service_object.save()
        return redirect("home")
    if request.method == "GET":
        service_object = Services.objects.get(serviceID=service_id)
        service_type = service_object.type
        context["service_type"] = service_type
    return render(request, "update_service_detail.html", context)


def search_vehicle(request):
    if request.method == "POST":
        vehicle_number = request.POST.get("vehicle_number")
        vehicle_object = get_object_or_404(Vehicle, pk=vehicle_number)
        if vehicle_object:
            data = {
                "vehicle_number": vehicle_object.vehicle_no,
                "model": vehicle_object.model,
                "brand": vehicle_object.brand
            }
            return JsonResponse(data)


def delete_vehicle(request):
    if request.method == "POST":
        vehicle_number = request.POST.get("vehicle_number")
        vehicle_object = get_object_or_404(Vehicle, pk=vehicle_number)
        if vehicle_object:
            vehicle_object.delete()
            return JsonResponse(data={"message": "vehicle deleted successfully"}, status=200)


def update_vehicle(request):
    if request.method == "POST":
        vehicle_number = request.POST.get("vehicle_number")
        vehicle_brand = request.POST.get("vehicle_brand")
        vehicle_model = request.POST.get("vehicle_model")
        vehicle_object = get_object_or_404(Vehicle, pk=vehicle_number)
        vehicle_object.brand = vehicle_brand
        vehicle_object.model = vehicle_model
        vehicle_object.save()
        return JsonResponse(data={"message": "vehicle details updated successfully"}, status=200)


def add_vehicle(request):
    if request.method == "POST":
        vehicle_number = request.POST.get("vehicle_number")
        vehicle_brand = request.POST.get("vehicle_brand")
        vehicle_model = request.POST.get("vehicle_model")
        if Vehicle.objects.filter(vehicle_no=vehicle_number):
            return JsonResponse(data={"message": "vehicle already exists", "status": 409}, status=409)
        Vehicle.objects.create(vehicle_no=vehicle_number, brand=vehicle_brand, model=vehicle_model).save()
        return JsonResponse(data={"message": "vehicle added successfully"}, status=200)


def add_service_detail(request):
    if request.method == "POST":
        service_id = request.POST.get("service_id")
        service_type = request.POST.get("service_type")
        vehicle_number = request.POST.get("vehicle_number")
        if Services.objects.filter(serviceID=service_id):
            return JsonResponse(data={"message": "service already exists"}, status=409)
        vehicle_object = Vehicle.objects.get(pk=vehicle_number)
        Services.objects.create(serviceID=service_id, type=service_type, vehicle_no=vehicle_object)
        return JsonResponse(data={"status": 200}, status=200)
