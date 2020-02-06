from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField()	
	class Meta:
		model = User
		fields = [
			"username",
			"email",
			"password1",
			"password2"
		]

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:	
		model = Profile
		fields = [
			'username',
			'email',

		]


class ProfileUpdateForm(forms.ModelForm):
	#username = forms.CharField()	
	# image = forms.FileField()
	class Meta:
		model = Profile
		fields = [
			'image',
			'diet_type',
			'calories_limit',
		]


