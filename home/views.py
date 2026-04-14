from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.db.models import F

# references
from .models import Stuff, Phone, Purchase, Sale
from .forms import StuffForm, PhoneForm, PurchaseForm, SaleForm


# Home start
def home(request):
    items = Phone.objects.filter(is_deleted=False).order_by("-created_at")
    return render(request, "home/index.html", {"items": items})


def open_phone_details(request, pk):
    item = Phone.objects.get(pk=pk)
    return render(request, "home/open_phone_details.html", {"item": item})


def add_phone(request):
    if request.method == "POST":
        form = PhoneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PhoneForm()

    return render(request, "home/add_phone.html", {"form": form})


def edit_phone(request, pk):
    phone = get_object_or_404(Phone, pk=pk)

    if request.method == "POST":
        form = PhoneForm(request.POST, request.FILES, instance=phone)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PhoneForm(instance=phone)

    return render(request, "home/edit_phone.html", {"form": form})


def delete_phone(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    phone.is_deleted = True
    phone.save()
    return redirect("home")


# home end


# Purchase start
def purchase_view(request):
    purchases = Purchase.objects.filter(is_deleted=False).order_by("-created_at")
    return render(request, "purchase/purchase.html", {"purchases": purchases})


def add_purchase_view(request):
    if request.method == "POST":
        form = PurchaseForm(request.POST)

        if form.is_valid():
            purchase = form.save()

            phone = purchase.phone
            phone.quantity += purchase.quantity
            phone.save()

            return redirect("purchase_view")

    else:
        form = PurchaseForm()

    return render(request, "purchase/add_purchase.html", {"form": form})

def edit_purchase_view(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)

    if request.method == "POST":
        form = PurchaseForm(request.POST, request.FILES, instance=purchase)
        if form.is_valid():
            form.save()
            return redirect("purchase_view")
    else:
        form = PurchaseForm(instance=purchase)

    return render(request, "purchase/edit_purchase.html", {"form": form})



def delete_purchase_view(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    purchase.is_deleted = True
    purchase.save()
    return redirect("purchase_view")


def open_purchase_details_view(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    phone = purchase.phone

    context = {
        "item": phone,
        "purchase": purchase,
    }
    return render(request, "purchase/open_purchase_details.html", context)


# Sale start
def sale_view(request):
    sales = Sale.objects.filter(is_deleted=False).order_by("-created_at")

    context = {
        "sales": sales,
    }
    return render(request, "sale/sale.html", context)


def add_sale_view(request):
    text = None

    if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            phone = sale.phone

            if phone.quantity >= sale.quantity:
                phone.quantity -= sale.quantity
                phone.save()
                sale.save()
                return redirect("sale_view")
            else:
                text = f"Telefonlar soni yetarli emas. Mavjud: {phone.quantity}"
    else:
        form = SaleForm()

    context = {
        "form": form,
        "text": text,
    }
    return render(request, "sale/add_sale.html", context)


def open_sale_details_view(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    phone = sale.phone

    context = {
        "item": phone,
        "sale": sale,
    }
    return render(request, "sale/open_sale_details.html", context)


def delete_sale_view(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    sale.is_deleted = True
    sale.save()
    return redirect("sale_view")

# Stuff
def stuff_view(request):
    stuff = Stuff.objects.filter(is_deleted=False)
    context = {
        "stuff": stuff
    }
    return render(request, "stuff/stuff.html", context)