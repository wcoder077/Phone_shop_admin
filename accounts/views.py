from django.shortcuts import render,redirect
from django.contrib.auth import  login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.decorators import login_not_required,login_required

# @login_not_required
# def register_view(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("home")
#     else:
#         form = UserCreationForm()
#     return render(request, "accounts/register.html", {"form":form})

@login_not_required
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form":form})

def logout_view(request):
    logout(request)
    return redirect("login_view")

@login_required(login_url="login_view")
def other(request):
    return render(request, "accounts/other.html")

@login_required(login_url="login_view")
def profile_update_view(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, "accounts/profile_edit.html", {"form": form})