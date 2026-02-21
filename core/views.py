from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return redirect("login")


@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            error = "Invalid username or password"
            return render(request, "auth/login.html", {"error": error})
    
    return render(request, "auth/login.html")


@require_http_methods(["GET", "POST"])
def signup_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()
        password_confirm = request.POST.get("password_confirm", "").strip()
        
        error = None
        
        if not username or not email or not password:
            error = "All fields are required"
        elif len(password) < 6:
            error = "Password must be at least 6 characters"
        elif password != password_confirm:
            error = "Passwords do not match"
        elif User.objects.filter(username=username).exists():
            error = "Username already exists"
        elif User.objects.filter(email=email).exists():
            error = "Email already exists"
        
        if error:
            return render(request, "auth/signup.html", {"error": error})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect("dashboard")
    
    return render(request, "auth/signup.html")


@login_required(login_url="login")
def dashboard(request):
    context = {
        "total_plans": 0,
        "total_campaigns": 0,
        "total_leads": 0,
        "total_budget": 0,
    }
    return render(request, "dashboard.html", context)


@require_http_methods(["POST"])
def logout_view(request):
    logout(request)
    return redirect("login")
