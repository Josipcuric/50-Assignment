from django.shortcuts import render
from .models import Parcel

def dashboard(request):
    return render(request, "logistics/dashboard.html")

def parcel_list(request):
    parcels = Parcel.objects.select_related("campaign", "destination").all()
    return render(request, "logistics/parcel_list.html", {"parcels": parcels})
