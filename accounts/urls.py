from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.decorators.cache import never_cache

from .views import dashboard, signup

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", never_cache(LoginView.as_view(template_name="accounts/registration/login.html")), name="login"),
    path("logout/", never_cache(LogoutView.as_view()), name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
]
