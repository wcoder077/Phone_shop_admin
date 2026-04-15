from django import forms
from .models import Stuff,Phone,Purchase,Sale,Reference

class StuffForm(forms.ModelForm):
    
    class Meta:
        model = Stuff
        fields = ("full_name","role", "departure_date", "phone","salary","photo",)

class PhoneForm(forms.ModelForm):
    
    class Meta:
        model = Phone
        fields = ("picture","name","brand","price","release_year", "display_size","resolution","cpu", "ram", "memory","rear_camera","front_camera", "battery","weight", "color", "material","description", "quantity")

class PurchaseForm(forms.ModelForm):
    
    class Meta:
        model = Purchase
        fields = ("phone","quantity", "cost_price", "description",)

class SaleForm(forms.ModelForm):
    
    class Meta:
        model = Sale
        fields = ("phone","quantity", "price_sold","payment_method","description",)
