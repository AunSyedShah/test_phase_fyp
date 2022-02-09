from django.db import models


# Create your models here.
class Vehicle(models.Model):
    vehicle_no = models.CharField(max_length=12, primary_key=True, default="")
    brand = models.CharField(max_length=25, default="")
    model = models.CharField(max_length=12, default="")

    def __str__(self):
        return self.vehicle_no


class Services(models.Model):
    serviceID = models.IntegerField(primary_key=True, default=0)
    type = models.CharField(max_length=10)
    vehicle_no = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.serviceID)
