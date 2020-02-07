from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse


from .models import Products ,Meals
from .forms import ProductForm, MealCreationForm, MealUpdateForm, MealQuantityUpdate



class ProductsTableView(ListView, SuccessMessageMixin):
    model = Products
    template_name = "Food/product_table.html"
    context_object_name = "object" #by default it's object_list 
    paginate_by = 10
    
    def get_context_data(self, **kwargs):      
        msg_storage = messages.get_messages(self.request)
        context = super().get_context_data(**kwargs)
        context['message'] = msg_storage
        return context
    

class ChosenDietProductsTableView(ListView):
    model = Products
    template_name = "Food/product_table_diet.html"
    context_object_name = "object" 
    paginate_by = 10

    def get_queryset(self):
        food_type = self.kwargs.get("food_type", "")     
        return Products.objects.filter(food_type=food_type)


class ProductDetailView(DetailView):
    model = Products
    template_name="Food/product_description.html"


class ProductUpdateView(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = Products
    template_name = "Food/product_update.html"
    fields = ["name", "protein", "carbohydrates", "fat", "description", "quantity", "food_type" ]
    def get_context_data(self, **kwargs):      
        message = messages.success(self.request, f"Product description updated") 
        context = super().get_context_data(**kwargs)
        context['message'] = message
        return context

    


class ProductCreateView(LoginRequiredMixin, FormView):
    model = Products
    template_name = "Food/product_add.html"
    form_class = ProductForm
    success_url = reverse_lazy("prod_table")

    def form_valid(self, form, **kwargs):
        new_prod_name = form.cleaned_data["name"].lower()        
        try:
            new_prod = Products.objects.get(name=new_prod_name)
            messages.warning(self.request, f'Product {new_prod_name} already exist.')
        except Products.DoesNotExist:
            new_prod = Products(
                name = form.cleaned_data["name"],
                protein = form.cleaned_data["protein"],
                carbohydrates =form.cleaned_data["carbohydrates"],
                fat = form.cleaned_data["fat"],
                description = form.cleaned_data["description"],
                quantity = form.cleaned_data["quantity"],
                price = form.cleaned_data["price"],
                food_type = form.cleaned_data["food_type"]
                )
            new_prod.save()  
            messages.success(self.request, f"New product: {new_prod_name} has been added.") 
        return redirect(reverse_lazy("prod_table"))



class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Products
    template_name = "Food/product_delete.html"
    success_url = reverse_lazy("prod_table")
    def test_func(self):
        if "admin" in str(self.request.user).lower():
            return True
        else: 
            return False 
    def get_context_data(self, **kwargs):      
        message = messages.warning(self.request, f"Product has been deleted.") 
        context = super().get_context_data(**kwargs)
        context['message'] = message
        return context


class MealTableView(ListView, SuccessMessageMixin):
    model = Meals
    template_name = "Food/meal_list_view.html"
    context_object_name = "object"
    paginate_by = 10

    def get_context_data(self, **kwargs):      
        msg_storage = messages.get_messages(self.request)
        context = super().get_context_data(**kwargs)
        context['message'] = msg_storage
        return context


class MealCreateView(LoginRequiredMixin, FormView):
    model = Meals
    template_name = "Food/meal_creation.html"
    form_class = MealCreationForm
    success_url = reverse_lazy("meal_table")
    
    def form_valid(self, form):
        meal_name = form.cleaned_data["name"].lower()
        new_meal, status = Meals.objects.get_or_create(name = meal_name)
        ingredient = Products.objects.filter(pk__in=form.cleaned_data["ingredient"])
        if status:
            new_meal.description =form.cleaned_data["description"] 
            new_meal.save()
            for ing in ingredient:
                #product = Products.objects.filter(name = ing).first()
                #new_meal.ingredient.add(product)
                new_meal.ingredient.add(ing)                
                new_meal.ingredients_weights = new_meal.ingredients_weights + str(ing.quantity) + ","
            if new_meal.ingredients_weights[-1] == ",":
                new_meal.ingredients_weights = new_meal.ingredients_weights[0:-1]
            new_meal.save()
        else:
            messages.warning(self.request, f'Meal called "{meal_name}" already exist in database.')

        return redirect(reverse_lazy("meal_table"))


class MealDetailView(DetailView):
    model = Meals
    template_name = "Food/meal_detail.html"

class MealDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Meals
    template_name = "Food/meal_delete.html"
    success_url = reverse_lazy("meal_table")

    def test_func(self):
        if "admin" in str(self.request.user).lower():
            return True
        else: 
            #return False 
            return redirect("meal_detail", pk=self.kwargs['pk'])

class MealDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Meals
    template_name = "Food/meal_delete.html"
    success_url = reverse_lazy("meal_table")

    def test_func(self):
        if "admin" in str(self.request.user).lower():
            return True
        else: 
            return False 


class MealUpdateDescription(LoginRequiredMixin, UpdateView):
    model = Meals
    template_name = "Food/meal_update.html"
    success_url = reverse_lazy("meal_table")
    fields = ["description"]



def remove_ingredient(request, pk, name):
    meal = Meals.objects.get(pk=pk)
    product = Products.objects.get(name=name)

    weight_index_to_be_deleted=0    
    for i, prod in enumerate(meal.get_all_ingredients()):
        if prod == product:
            weight_index_to_be_deleted = i
            break
    ingredients_weights = meal.ingredients_weights
    coma_positions =[]

    if "," not in ingredients_weights:  
        ingredients_weights = ""
    else:
        for i in range(len(ingredients_weights)):
            if ingredients_weights[i] ==",":
                coma_positions.append(i)
        if weight_index_to_be_deleted == 0:
            ingredients_weights = ingredients_weights[coma_positions[weight_index_to_be_deleted]+1:]
        elif weight_index_to_be_deleted == len(coma_positions):
            ingredients_weights = ingredients_weights[:coma_positions[weight_index_to_be_deleted-1]]
        else:
            ingredients_weights = ingredients_weights[:coma_positions[weight_index_to_be_deleted-1]] + ingredients_weights[coma_positions[weight_index_to_be_deleted]:]

    meal.ingredients_weights  = ingredients_weights
    meal.save()
    meal.ingredient.remove(product)
    return redirect("meal_detail", pk=pk)

class UpdateIngredientQuantity(FormView):
    model = Meals
    template_name = "Food/meal_quantity_update.html"
    success_url = reverse_lazy("meal_table")
    form_class = MealQuantityUpdate

    def form_valid(self, form):
        meal = Meals.objects.get(pk=self.kwargs['pk'])
        ingredients_weights = meal.ingredients_weights
        new_quantity = form.cleaned_data["Weight"] 
        weight_to_be_changed = self.kwargs['index']
        ingredients_weights = meal.ingredients_weights
        coma_positions =[]

        for i in range(len(ingredients_weights)):
            if ingredients_weights[i] ==",":
                coma_positions.append(i)

        if weight_to_be_changed == 0:
            ingredients_weights =  new_quantity #+ "," + ingredients_weights[coma_positions[weight_to_be_changed]+1:]
        elif weight_to_be_changed == len(coma_positions):
            ingredients_weights = ingredients_weights[:coma_positions[weight_to_be_changed-1]] + "," + new_quantity
        else:
            ingredients_weights = ingredients_weights[:coma_positions[weight_to_be_changed-1]] + "," + new_quantity +  ingredients_weights[coma_positions[weight_to_be_changed]:]

        meal.ingredients_weights  = ingredients_weights
        meal.save()   
        
        return redirect("meal_detail", pk=self.kwargs['pk'])























# #OLD ONES
# from django.shortcuts import render,redirect
# from django.contrib.auth.decorators import login_required
# from .forms import ProductForm

# def product_view(request):
#   obj = Products.objects.all()
#   context = {"obj":obj}
#   return render(request, "Food/product_description.html", context)    


# def products_table_view(request):
#   context = {"obj":Products.objects.all()}    
#   return render(request, "Food/product_table.html", context)

# def meal_view(request):
#   obj = Meals.objects.all()
#   context = {"obj":obj}
#   return render(request, "Food/meal_description.html", context)
    
# def meal_table_view(request):
#   context = {"obj":Meals.objects.all()}   
#   return render(request, "Food/product_table.html", context)


# @login_required(login_url='/user/login/')
# def add_product(request): 
#   #request.POST built-in validation for Django forms.
#   form = ProductForm() #forms.cleaned_data => dane formularza !! #Default value == GET
#   if request.method == "POST":        
#       form = ProductForm(request.POST)
#       if form.is_valid():
#               Products.objects.create(**form.cleaned_data) ##wartosc przekazywana w formie slownika z formsow- trzeba rozpakowac
#               #print(form.cleaned_data)
#               form = ProductForm() #Will "restart" our form. 
#       else:
#           redirect("prod_table")
#           #print(form.errors) 
#   context = {"form": form}            
#   return render(request,"Food/add_product.html", context)
#   #return redirect('food/desc')#Tu bedzie przekierowanie do description

# @login_required(login_url='/user/login/')
# def meal_add(request):
#   return render(request,"Food/meal_product.html")


