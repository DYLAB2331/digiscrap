from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
        
    else:
        form = UserCreationForm()
    
    return render(request, "register.html", {"form": form})


# TODO: Implement custom login page using Authentication Form
# Old login view using AuthenticationForm
# def loginView(request):
#     if request.method == "POST":
#         form = AuthenticationForm(data=request.POST)

#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect("dashboard")
        
#     else:
#         form = AuthenticationForm()

#     return render(request, "login.html", {"form": form})

def loginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, "login.html", {"error": "Invalid username or password"})
        else:
            login(request, user)
            return redirect("dashboard")
        
    return render(request, "login.html", {})

def logoutView(request):
    logout(request)
    return redirect("login")

@login_required
def dashboardView(request):
    photos = Photo.objects.filter(user=request.user)
    return render(request, "dashboard.html", {"photos": photos})

# Photo upload and display implementation

from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoForm

@login_required
def uploadPhotoView(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect("dashboard")
        
    else:
        form = PhotoForm()
    
    return render(request, "photoUpload.html", {"form": form})

# Photo deletion

@require_POST
def deletePhotoView(request):
    photoIDs = request.POST.getlist("photoIDs")
    photosSelected = Photo.objects.filter(id__in=photoIDs, user=request.user)

    for photo in photosSelected:
        photo.image.delete(save=True)
        photo.delete()
        
    return redirect("dashboard")