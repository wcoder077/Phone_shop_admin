from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Base urls
    path("", views.home , name="home"),
    path("add/", views.add_phone , name="add_phone"),
    path("edit/<int:pk>/", views.edit_phone , name="edit_phone"),
    path("delete/<int:pk>/", views.delete_phone , name="delete_phone"),
    path("open_details/<int:pk>/", views.open_phone_details , name="open_phone_details"),
    # Base urls end

    # Purchase
    path("purchase/", views.purchase_view, name="purchase_view"),
    path("purchase/add_purchase/", views.add_purchase_view, name="add_purchase_view"),
    path("purchase/delete_purchase/<int:pk>/", views.delete_purchase_view, name="delete_purchase_view"),
    path("purchase/purchase_details/<int:pk>/", views.open_purchase_details_view, name="open_purchase_details_view"),
    
    # Sale
    path("sale/", views.sale_view, name="sale_view"),
    path("sale/add_sale/", views.add_sale_view, name="add_sale_view"),
    path("sale/delete_sale/<int:pk>/", views.delete_sale_view, name="delete_sale_view"),
    path("sale/sale_details/<int:pk>/", views.open_sale_details_view, name="open_sale_details_view"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)