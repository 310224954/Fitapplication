from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.db import IntegrityError
from datetime import date
from django.urls import reverse_lazy

from .models import Profile, UserProd, Diet
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from Food.models import Products, Meals


def registration_view(request):
    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            messages.success(request, f"Account Created for {username}")
            return redirect("login")
    else:
        form = UserRegistrationForm()
    context = {"form":form}
    return render(request, "Users/registration.html", context)


def profile_view(request):
    user_form=UserUpdateForm
    profile_form=ProfileUpdateForm
    if request.POST:
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f"Your profile has been updated!")
            return redirect('profile')
    else:       
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'user_form':user_form,
        'profile_form':profile_form
    }
    return render(request, "Users/profile.html", context)

class DietView(ListView):
    model = Diet
    template_name = "Users/Diet/user_diet_view.html"


class ChangeDietQuantity(UpdateView):
    model = UserProd
    template_name = "Users/Diet/user_diet_edit.html"
    fields = ["diet_quantity"]
    success_url = reverse_lazy("diet_plan")

class DeteProdFromDiet(DeleteView):
    model = UserProd
    template_name = "Users/Diet/user_diet_delete_position.html"
    success_url = reverse_lazy("diet_plan")


@login_required
def add_prod_to_diet(request, pk):
    user_profile = Profile.objects.get(user = request.user)
    product = Products.objects.filter(pk = pk).first()
    user_product, prod_created = UserProd.objects.get_or_create(prod=product, unique_number=user_profile.pk)
    if not prod_created:        
        user_product.diet_quantity += product.quantity      
        user_product.save()
    else:
        user_product.diet_quantity=product.quantity
        user_product.save()
    user_diet, diet_created = Diet.objects.get_or_create(profile_user=user_profile)
    user_diet.diet_prod.add(user_product)
    if diet_created:
        user_diet.save()  
    messages.info(request, f"Product {product} has been added to your diet_plan.")
    return HttpResponse(status=204)




#Workign one but not connecting
# @login_required
# def add_prod_to_diet(request, pk):
#     user_profile = Profile.objects.get(user = request.user)     

#     product = Products.objects.filter(pk = pk).first()
#     user_product, prod_created = UserProd.objects.get_or_create(prod=product)
#     if not prod_created:      
#       user_product.diet_quantity += product.quantity      
#       user_product.save()
#     else:
#       user_product.diet_quantity=product.quantity
#       user_product.save()
#     user_diet, diet_created = Diet.objects.get_or_create(profile_user=user_profile)
#     user_diet.diet_prod.add(user_product)
#     if diet_created:
#       user_diet.unique_number = "" + str(date.today().day) + str(date.today().month) + str(user_profile.pk)           
#       user_diet.save()
#     messages.info(request, f"Product {product} has been added to your diet plan.")
#     return HttpResponse(status=204)


# @login_required
# def add_prod_to_diet(request, pk):
#   user_profile = Profile.objects.get(user = request.user) 
#   product = Products.objects.filter(pk = pk)
#   user_product = UserProd(prod=product,diet_quantity=product.values("quantity"))

#   diet_item = Diet.objects.get_or_create(profile_user=user_profile, )#, profile_user=user_profile prod=product,
#   diet_item.prod.add(user_product)
#   try:
#       diet_item.save()
#   except IntegrityError:
#       for i in UserProd.objects.all():
#           if diet_item.prod.name == i.prod.name:              
#               diet_item = UserProd.objects.get(pk=i.pk)
#               #diet_item.diet_quantity += product.quantity
#               diet_item.diet_quantity += product.values["quantity"]
#               #print(diet_item.profile_user)
#               diet_item.save()            
#   messages.info(request, f"Product {product} has been added to your diet plan.")
#   return HttpResponse(status=204)

# #Order_item == UserProd
# #Order == Diet

# def get_choosen_products(request):
#   profile_user = Profile.objects.get(user = request.user)
#   diet_items = Diet.objects.filter(profile_user=profile_user)
#   if diet_items.exist():
#       return diet_items[0]
#   return 0

# @login_required
# def diet_view(request, **kwargs):
#   return render(request, "Users/Diet/user_diet_view.html",get_choosen_products(request))

# @login_required
# #def add_prod_to_diet(request, **kwargs):
# def add_prod_to_diet(request, pk):
#   user_profile = get_object_or_404(Profile, user=request.user)
#   #product = Products.objects.filter(id=kwargs.get("item_id", "")).first()
#   product = Products.objects.get(pk=pk)
#   new_item = UserProd.objects.get_or_create(pk=product.pk, prod=product.name)
#   diet = Diet.objects.get_or_create(owner=user_profile)
#   diet.items.add(new_item)
#   messages.info(request, f"product {new_item} added to your diet plan.")
#   return redirect("prod_table")

    #food = get_object_or_404(Products, pk=pk) #getting product 
    # item = Products.objects.get(pk = pk)  
    # new_prod = UserProd(profile_user=request.user, prod_name=item.name)
    # new_prod.save()
    # messages.add_message(request, messages.INFO, "Product added!")
    # return redirect("prod_table")

















































