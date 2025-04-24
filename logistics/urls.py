from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('parcels/', views.parcel_list, name='parcel_list'),
]
