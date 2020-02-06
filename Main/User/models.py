from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from datetime import date

from Food.models import Products, Meals



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE) # CASCADE: delete user => delete profile
	image = models.ImageField(default='default.jpg', upload_to='profile_pictures')#pip install Pillow require for handling images in Django
	username = models.CharField(max_length=50)
	diet_type = models.CharField(max_length=5, choices=(
		("1", "Vegan"),
		("2", "Vegeterian"),
		("3", "Paleo"), 
		("4", "Keto"),
		("5", "None")
		), default="5"
	)	
	def __str__(self):
		return f'{self.user.username} Profile'
	calories_limit= models.IntegerField(default=2500, blank=True, null=True)


class UserProd(models.Model):   
	#prod = models.OneToOneField(Products, on_delete=models.SET_NULL, null=True)#Prevents creation of more than 1 Product instance
	prod = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
	date = models.TimeField(auto_now_add=True)  
	diet_quantity = models.IntegerField(default=100)
	unique_number = models.CharField(max_length=10)

	def __str__(self):
		return f"{self.prod.name} - {self.diet_quantity} - {self.unique_number}"

	@property
	def prod_protein(self):
		return round(self.prod.protein * self.diet_quantity / 100,2)

	@property
	def prod_carbohydrates(self):
		return round(self.prod.carbohydrates * self.diet_quantity / 100,2)

	@property
	def prod_fat(self):
		return round(self.prod.fat * self.diet_quantity / 100,2)

	@property
	def prod_price(self):
		return self.prod.price * self.diet_quantity / 100


class Diet(models.Model):   
	profile_user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True) 
	date = models.TimeField(auto_now=True)
	diet_prod = models.ManyToManyField(UserProd, related_name="diet_set")#related_name="<class>_set" by default.

	def __str__(self):
		return str(self.profile_user)

	
	def get_all_prods(self):
		return self.diet_prod.all()	
	
	@property
	def get_diet_carbohydrates(self):
		return int(sum([diet_prod.prod_carbohydrates for diet_prod in self.diet_prod.all()]))
	@property
	def get_diet_fat(self):
		return int(sum([diet_prod.prod_fat for diet_prod in self.diet_prod.all()]))
	@property
	def get_diet_price(self):
		return int(sum([diet_prod.prod_price for diet_prod in self.diet_prod.all()]))
	@property
	def get_diet_proteins(self):
		return int(sum([diet_prod.prod_protein for diet_prod in self.diet_prod.all()]))

	@property
	def get_diet_callories(self):
		return int(sum([self.get_diet_carbohydrates*4, self.get_diet_fat*8, self.get_diet_proteins*4]))
























# class UserMeal(models.Model):
#   profile_user = models.OneToOneField(User, on_delete=models.CASCADE)
#   meal_name = models.CharField(max_length=40)
#   date = models.TimeField(default=date.today)



	# 
	# def protein_sum(self):    
	#   return UserProd.objects.aggregate(Sum('prod_protein'))
	#   #ItemPrice.objects.aggregate(Sum('price'))
		#return sum([item.prod_protein for item in UserProd.objects.all()])
		#return sum([item.product.price for item in self.prod.all()])
		#return sum([item.prod_protein for item in self.prod.all()])
		# return self.prod.aggregate(Sum("protein"))["protein_sum"]









	# protein = models.FloatField()
	# carbohydrates = models.FloatField()
	# fat = models.FloatField()
	# quantity = models.IntegerField(blank=True)
	# price = models.DecimalField(max_digits=100, decimal_places=2, blank=True)
	
	
	
	
	# def __str__(self):
	#   return self.date

	# 
	# def total_protein(self):
	#   return (self.individual_prods.aggregate(Sum("protein"))["protein_sum"] + self.prep_meals.aggregate(Sum("protein"))["protein_sum"])

	# 
	# def total_fat(self):
	#   return (self.individual_prods.aggregate(Sum("fat"))["fat_sum"] + self.prep_meals.aggregate(Sum("protein"))["fat_sum"])

	# 
	# def total_carbohydrates(self):
	#   return (self.individual_prods.aggregate(Sum("carbohydrates"))["carbohydrates_sum"] + self.prep_meals.aggregate(Sum("carbohydrates"))["carbohydrates_sum"])  









