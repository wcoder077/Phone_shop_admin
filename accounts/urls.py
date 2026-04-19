from django.urls import path

from . import views

urlpatterns = [
    path("", views.other, name="other"),
    path("register/", views.register_view, name="register_view"),
    path("login/", views.login_view, name="login_view"),
    path("logout/", views.logout_view, name="logout_view"),
    path("profile/edit/", views.profile_update_view, name="profile_update_view"),
]