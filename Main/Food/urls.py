from django.urls import path, re_path
from .views import (
	ProductsTableView,
	ProductDetailView,
	ProductUpdateView,
	ProductCreateView,
	ProductDeleteView,
	######MEALS#######
	MealTableView,
	MealCreateView,
	MealDetailView,
	MealUpdateDescription,
	MealDeleteView,
	ChosenDietProductsTableView,
	remove_ingredient,
	UpdateIngredientQuantity
	)
from User.views import add_prod_to_diet


urlpatterns = [
	path("", ProductsTableView.as_view(), name="prod_table"),
	path("product_add/",ProductCreateView.as_view(), name="prod_add"),
	path("product_desc/<int:pk>/",ProductDetailView.as_view(), name="prod_desc"),
	path("product_desc/<int:pk>/update",ProductUpdateView.as_view(), name="prod_update"),
	path("product_desc/<int:pk>/delete",ProductDeleteView.as_view(), name="prod_delete"),	
	path("<food_type>/", ChosenDietProductsTableView.as_view(), name="filter_food_table"),
	#######MEALS#########
	path("food/meals/",MealTableView.as_view(), name="meal_table" ),
	path("meal/create/",MealCreateView.as_view(), name="meal_create" ),		
	path("meal_detail/<int:pk>/delete",MealDeleteView.as_view(), name="meal_delete"),
	path("product_add/<int:pk>/",add_prod_to_diet, name="add_to_diet"),
	path("meal_detail/<int:pk>/edit",MealUpdateDescription.as_view(), name="desc_meal_update"),
	#########################
	path("meal_detail/<int:pk>/",MealDetailView.as_view(), name="meal_detail" ),
	path("meal_detail/<int:pk>/remove/<str:name>", remove_ingredient, name="remove_ingredient"),	
	path("meal_detail/<int:pk>/update_quantity/<int:index>", UpdateIngredientQuantity.as_view(), name="update_meal_quantity"),

]




