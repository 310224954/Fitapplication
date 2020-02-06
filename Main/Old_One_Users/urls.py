from django.urls import path, include

from .views import registration_view, login_view, logout_view

urlpatterns = [
    path("registration/", registration_view, name="registration_view"),
    path("login/", login_view),
    path("logout/", logout_view)
    ]