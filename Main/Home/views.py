from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
	#return HttpResponse("<h1>Welcome to my fit django website</h1>")
	context = {}
	return render(request, "Home/home.html", context)

def contact_view(request):
	return render(request, "Home/contact.html", {})
	#return HttpResponse("<h1>Please call me</h1>")


def ciriculum_vitae_view(request):
	pass

def socai_media(request):
	pass