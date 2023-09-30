from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.views.decorators.http import require_POST
from django.core.exceptions import ValidationError
from django.http import JsonResponse

# Create your views here.

def redirectToLogin(request):
    return redirect('login')

def registerView(request):
    context = {}

    if request.method == "POST":
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        passwordConfirm = request.POST.get("password2")

        context['firstName'] = firstName
        context['lastName'] = lastName
        context['email'] = email
        context['username'] = username
        context['password'] = password

        if password == passwordConfirm:
            # Password validation using built in validate_password() and ValidationError
            try:
                validate_password(password)
            except ValidationError as errorPass:
                context["error"] = errorPass.messages
                return render(request, "register.html", context)
            
            # Check to see if user already has an account
            if User.objects.filter(username=username).exists():
                context["error"] = "Username already exists"
                return render(request, "register.html", context)
            elif User.objects.filter(email=email).exists():
                context["error"] = "Email already exists"
                return render(request, "register.html", context)
            else:
                user = User.objects.create_user(first_name=firstName, last_name=lastName, email=email, username=username, password=password)
                login(request, user)
                return redirect("dashboard")
        else:
            context["error"] = "Passwords do not match"
            return render(request, "register.html", context)
    
    return render(request, 'register.html', context)

def loginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is None:
            context = {"error": "Invalid username or password"}
            return render(request, "login.html", context)
        else:
            login(request, user)
            return redirect("dashboard")
        
    return render(request, "login.html", {})

def logoutView(request):
    logout(request)
    return redirect("login")

@login_required
def dashboardView(request):
    photos = Photo.objects.filter(users=request.user)
    return render(request, "dashboard.html", {"photos": photos})

# Photo upload  
from .models import Photo
from .forms import UploadPhotoForm

@login_required
def uploadPhotoView(request):
    if request.method == "POST":
        form = UploadPhotoForm(request.POST, request.FILES)

        if form.is_valid():
            photo = form.save()
            photo.users.add(request.user)
            return redirect("dashboard")
        
    else:
        form = UploadPhotoForm()
    
    return render(request, "photoUpload.html", {"form": form})

# Photo sharing
@require_POST
def sharePhotoView(request):
    if request.method == "POST":

        usernameShare = request.POST.get("username")

        try:
            usernameShare = User.objects.get(username=usernameShare)
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Username does not exist'})
        
        user = request.user
        photos = Photo.objects.filter(users=user)

        for photo in photos:
            photo.users.add(usernameShare)
            photo.save()

        return JsonResponse({'status': 'success', 'message': 'Photos shared successfully'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

# Photo deletion
@require_POST
def deletePhotoView(request):
    photoIDs = request.POST.getlist("photoIDs")
    photosSelected = Photo.objects.filter(id__in=photoIDs, user=request.user)

    for photo in photosSelected:
        photo.image.delete(save=True)
        photo.delete()
        
    return redirect("dashboard")


# def registerView(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect("login")
        
#     else:
#         form = UserCreationForm()
    
#     return render(request, "register.html", {"form": form})


# TODO: Implement custom login page using AuthenticationForm
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