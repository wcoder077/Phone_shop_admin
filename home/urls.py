from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # search_view
    path("search/", views.search_view, name="search_view"),
    path("live-search/", views.live_search, name="live_search"),
    
    # Base urls
    path("", views.home , name="home"),
    path("add_phone/", views.add_phone , name="add_phone"),
    path("edit_phone/<int:pk>/", views.edit_phone , name="edit_phone"),
    path("delete_phone/<int:pk>/", views.delete_phone , name="delete_phone"),
    path("open_phone_details/<int:pk>/", views.open_phone_details , name="open_phone_details"),
    # Base urls end

    # Purchase
    path("purchase/", views.purchase_view, name="purchase_view"),
    path("purchase/edit_purchase/<int:pk>/", views.edit_purchase_view, name="edit_purchase_view"),
    path("purchase/add_purchase/", views.add_purchase_view, name="add_purchase_view"),
    path("purchase/delete_purchase/<int:pk>/", views.delete_purchase_view, name="delete_purchase_view"),
    path("purchase/purchase_details/<int:pk>/", views.open_purchase_details_view, name="open_purchase_details_view"),
    
    # Sale
    path("sale/", views.sale_view, name="sale_view"),
    path("sale/add_sale/", views.add_sale_view, name="add_sale_view"),
    path("sale/edit_sale/<int:pk>/", views.edit_sale_view, name="edit_sale_view"),
    path("sale/delete_sale/<int:pk>/", views.delete_sale_view, name="delete_sale_view"),
    path("sale/sale_details/<int:pk>/", views.open_sale_details_view, name="open_sale_details_view"),
    
    # Stuff
    path("stuff/", views.stuff_view, name="stuff_view"),
    path("stuff/edit_stuff/<int:pk>/", views.edit_stuff_view, name="edit_stuff_view"),
    path("stuff/add_stuff/", views.add_stuff_view, name="add_stuff_view"),
    path("stuff/delete_stuff/<int:pk>/", views.delete_stuff_view, name="delete_stuff_view"),
    path("stuff/open_stuff_details/<int:pk>/", views.open_stuff_details_view, name="open_stuff_details_view"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)