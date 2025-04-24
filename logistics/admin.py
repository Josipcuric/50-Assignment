from django.contrib import admin
from .models import Campaign, Content, Parcel, ContentInParcel, Destination

admin.site.register(Campaign)
admin.site.register(Content)
admin.site.register(Parcel)
admin.site.register(ContentInParcel)
admin.site.register(Destination)
