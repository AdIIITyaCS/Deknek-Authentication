from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache

from .forms import SignUpForm
from .models import UserProfile


@never_cache
def home(request):
    return render(request, "accounts/home.html")


@never_cache
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = ""
            user.save()
            UserProfile.objects.create(
                user=user,
                full_name=form.cleaned_data["full_name"],
                email=form.cleaned_data["email"],
                phone_number=form.cleaned_data["phone_number"],
                address=form.cleaned_data["address"],
            )
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect("dashboard")
    else:
        form = SignUpForm()

    return render(request, "accounts/registration/signup.html", {"form": form})


@never_cache
@login_required
def dashboard(request):
    profile = getattr(request.user, "profile", None)
    return render(request, "accounts/dashboard.html", {"profile": profile})
