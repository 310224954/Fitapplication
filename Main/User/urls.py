from django.urls import path, include
from django.contrib.auth import views

from .views import (
	registration_view, 
	profile_view,
	DietView,
	ChangeDietQuantity,
	DeteProdFromDiet,
)

urlpatterns = [
	#Registration and profile creation Url's
	path("", registration_view, name="registration"),
	path("login/", views.LoginView.as_view(template_name="Users/login.html"), name="login"),
	path("logout/", views.LogoutView.as_view(template_name="Users/logout.html"), name="logout"),
	path("profile/", profile_view, name="profile"),
	#Diet plan Url's
	path("diet_plan/", DietView.as_view(), name="diet_plan"),
	path("diet_plan/edit/<int:pk>/", ChangeDietQuantity.as_view(), name="edit_user_prod"),
	path("diet_plan/delete/<int:pk>/", DeteProdFromDiet.as_view(), name="delete_user_prod"),

	#Username password restart Url's
	path("password_reset/", views.PasswordResetView.as_view(template_name="Users/password_reset.html"), name="password_reset"),
	path("password_reset/done/", views.PasswordResetDoneView.as_view(template_name="Users/password_reset_done.html"), name="password_reset_done"),
	path("password_reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(template_name="Users/password_change.html"), name="password_reset_confirm"),
	path("password_reset/changed/done/", views.PasswordResetCompleteView.as_view(template_name="Users/password_reset_complete.html"), name="password_reset_complete"),
]