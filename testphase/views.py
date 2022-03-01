from django.http import JsonResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import Vehicle, Services


# Create your views here.
def index(request):
    return render(request, "index.html")


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


def get_vehicle_details(request):
    if request.method == "POST":
        services = Services.objects.filter(vehicle_no=request.POST.get("vehicle_number")).values("serviceID", "type")
        return JsonResponse(data={"services": list(services)})


def delete_vehicle_details(request, service_id):
    if request.method == "GET":
        Services.objects.get(pk=service_id).delete()
        return JsonResponse(data={}, status=200)


def update_vehicle_detail(request):
    if request.method == "POST":
        service_id = request.POST.get("service_id")
        service_object = Services.objects.get(pk=service_id)
        service_object.type = request.POST.get("service_type")
        service_object.save()
        return JsonResponse(data={}, status=200)
