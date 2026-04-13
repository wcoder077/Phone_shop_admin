from django.contrib import admin
from .models import Reference, Phone, Purchase, Stuff, Sale

admin.site.register(Reference)
admin.site.register(Phone)
admin.site.register(Stuff)
admin.site.register(Purchase)
admin.site.register(Sale)