from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db import transaction
from django.db.models import F, Q
from django.contrib.auth.decorators import login_not_required, login_required

# references
from .models import Stuff, Phone, Purchase, Sale
from .forms import StuffForm, PhoneForm, PurchaseForm, SaleForm,Reference

# Home start
@login_required(login_url="login_view")
def home(request):
    items = Phone.objects.filter(is_deleted=False).order_by("-created_at")
    return render(request, "home/index.html", {"items": items})

@login_required(login_url="login_view")
def open_phone_details(request, pk):
    item = Phone.objects.get(pk=pk)
    return render(request, "home/open_phone_details.html", {"item": item})

@login_required(login_url="login_view")
def add_phone(request):
    if request.method == "POST":
        form = PhoneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PhoneForm()

    return render(request, "home/add_phone.html", {"form": form})

@login_required(login_url="login_view")
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
@login_required(login_url="login_view")
def purchase_view(request):
    purchases = Purchase.objects.filter(is_deleted=False).order_by("-created_at")
    return render(request, "purchase/purchase.html", {"purchases": purchases})

@login_required(login_url="login_view")
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

@login_required(login_url="login_view")
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

@login_required(login_url="login_view")
def open_purchase_details_view(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    phone = purchase.phone

    context = {
        "item": phone,
        "purchase": purchase,
    }
    return render(request, "purchase/open_purchase_details.html", context)


# Sale start
@login_required(login_url="login_view")
def sale_view(request):
    sales = Sale.objects.filter(is_deleted=False).order_by("-created_at")

    context = {
        "sales": sales,
    }
    return render(request, "sale/sale.html", context)

@login_required(login_url="login_view")
def add_sale_view(request):
    if request.method == "POST":
        form = SaleForm(request.POST)

        if form.is_valid():
            sale = form.save(commit=False)
            phone = sale.phone

            if phone.quantity >= sale.quantity:
                Phone.objects.filter(pk=phone.pk).update(
                    quantity=F("quantity") - sale.quantity
                )

                sale.save()
                return redirect("sale_view")
            else:
                form.add_error(
                    "quantity",
                    f"Telefonlar soni yetarli emas. Mavjud: {phone.quantity}",
                )
    else:
        form = SaleForm()

    return render(request, "sale/add_sale.html", {"form": form})

@login_required(login_url="login_view")
def open_sale_details_view(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    phone = sale.phone

    context = {
        "item": phone,
        "sale": sale,
    }
    return render(request, "sale/open_sale_details.html", context)

@login_required(login_url="login_view")
def edit_sale_view(request, pk):
    sale = get_object_or_404(Sale, pk=pk)

    if request.method == "POST":
        form = SaleForm(request.POST, request.FILES, instance=sale)
        if form.is_valid():
            form.save()
            return redirect("sale_view")
    else:
        form = SaleForm(instance=sale)

    return render(request, "sale/edit_sale.html", {"form": form})


def delete_sale_view(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    sale.is_deleted = True
    sale.save()
    return redirect("sale_view")


# Stuff
@login_required(login_url="login_view")
def stuff_view(request):
    stuffs = Stuff.objects.filter(is_deleted=False)
    context = {"stuffs": stuffs}
    return render(request, "stuff/stuff.html", context)

@login_required(login_url="login_view")
def add_stuff_view(request):
    if request.method == "POST":
        form = StuffForm(request.POST)

        if form.is_valid():
            stuff = form.save()
            return redirect("stuff_view")

    else:
        form = StuffForm()

    return render(request, "stuff/add_stuff.html", {"form": form})

@login_required(login_url="login_view")
def edit_stuff_view(request, pk):
    stuff = get_object_or_404(Stuff, pk=pk)

    if request.method == "POST":
        form = StuffForm(request.POST, request.FILES, instance=stuff)
        if form.is_valid():
            form.save()
            return redirect("stuff_view")
    else:
        form = StuffForm(instance=stuff)

    return render(request, "stuff/edit_stuff.html", {"form": form})


def delete_stuff_view(request, pk):
    stuff = get_object_or_404(Stuff, pk=pk)
    stuff.is_deleted = True
    stuff.save()
    return redirect("stuff_view")

@login_required(login_url="login_view")
def open_stuff_details_view(request, pk):
    stuff = get_object_or_404(Stuff, pk=pk)
    context = {
        "stuff": stuff,
    }
    return render(request, "stuff/open_stuff_details.html", context)


# Search view
@login_required(login_url="login_view")
def search_view(request):
    query = request.GET.get("q", "").strip()

    stuffs = Stuff.objects.none()
    phones = Phone.objects.none()
    sales = Sale.objects.none()
    references = Reference.objects.none()

    if query:

        stuffs = Stuff.objects.filter(
            Q(full_name__icontains=query) |
            Q(phone__icontains=query) |
            Q(role__icontains=query)
        )

        phones = Phone.objects.filter(
            Q(name__icontains=query) |
            Q(material__icontains=query) |
            Q(rear_camera__icontains=query) |
            Q(front_camera__icontains=query) |
            Q(display_size__icontains=query) |
            Q(resolution__icontains=query) |
            Q(cpu__icontains=query) |
            Q(price__icontains=query) |
            Q(brand__value__icontains=query) |
            Q(ram__value__icontains=query) |
            Q(memory__value__icontains=query) |
            Q(color__value__icontains=query)
        ).distinct()

        sales = Sale.objects.filter(
            Q(phone__name__icontains=query) |
            Q(payment_method__icontains=query) |
            Q(description__icontains=query)
        ).distinct()

        references = Reference.objects.filter(
            Q(type__icontains=query) |
            Q(value__icontains=query)
        )

    return render(request, "search.html", {
        "query": query,
        "stuffs": stuffs,
        "phones": phones,
        "sales": sales,
        "references": references,
    })
@login_required(login_url="login_view")
def live_search(request):
    query = request.GET.get("q", "")

    phones = Phone.objects.filter(
        Q(name__icontains=query) |
        Q(brand__value__icontains=query)
    )[:10]

    data = [
        {
            "id": p.id,
            "name": p.name,
            "price": str(p.price),
            "image": p.picture.url if p.picture else ""
        }
        for p in phones
    ]

    return JsonResponse({"results": data})