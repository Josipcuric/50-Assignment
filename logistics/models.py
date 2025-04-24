from django.db import models
from django.contrib.auth.models import User

class Campaign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    manager = models.ForeignKey(User, on_delete=models.CASCADE)

class Content(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    file_path = models.FileField(upload_to='uploads/')
    status = models.CharField(max_length=50, default='Pending')
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

class Destination(models.Model):
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

class Parcel(models.Model):
    parcel_number = models.CharField(max_length=100)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='In Transit')

class ContentInParcel(models.Model):
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
