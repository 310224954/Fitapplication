from django.db import models
from django.contrib import messages
from django.db.models import Sum
from django.urls import reverse
from django.template.defaultfilters import slugify
from datetime import date

# food_types = (
#   ("1", "Meat"),
#   ("2", "Fruit"),
#   ("3", "Vegetable"), 
#   ("4", "SeaFood"),
#   ("5", "Nuts"),
#   ("6", "Grains"),
#   ("7", "Diary")
# )

class Products(models.Model):
    name = models.CharField(max_length=50)
    protein = models.FloatField()
    carbohydrates = models.FloatField()
    fat = models.FloatField()
    description = models.TextField(blank=True)
    quantity = models.IntegerField(blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, blank=True)
    #date = models.TimeField(default=date.today)
    date = models.TimeField(auto_now_add=True)  
    food_type = models.CharField(max_length=6, choices=(
        ("1", "Meat"),
        ("2", "Fruit"),
        ("3", "Vegetable"), 
        ("4", "SeaFood"),
        ("5", "Nuts"),
        ("6", "Grains"),
        ("7", "Diary")
        )
    )
    slug = models.CharField(
      max_length=20,         
      null= True,
      unique=True,
   )

    class Meta:
        ordering = ["name"] #order by its name descending order

    def save(self, *args, **kwargs):
        self.fat = round(self.fat, 1)
        self.protein = round(self.protein, 1)
        self.carbohydrates = round(self.carbohydrates, 1)
        if not self.slug:
            self.slug = slugify(self.name)
        self.name = self.name.lower()
        super(Products, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"#"{} - {}".format(self.name, self.get_food_type_display())

    @property
    def name_type(self):
        return "{} {}".format(self.name + self.food_type)
        

    @property   
    def short_description(self):
        description = self.description
        short_description = ""
        for i,element in enumerate(description):
            if(i > 30 and element==" "):
                break
            short_description += element
        short_description += " ..."
        return short_description
        
    def get_absolute_url(self):
        return reverse("prod_desc", kwargs={"pk":self.pk})#, "slug":self.slug
        



class Meals(models.Model):
    name = models.CharField(max_length=40)
    ingredient = models.ManyToManyField(Products, related_name="products")
    description = models.TextField(blank=True, max_length=750)
    ingredients_weights = models.CharField(max_length=40, blank=True)
    slug = models.CharField(
      max_length=81,         
      blank= True,
      unique=True,
   )

    @property
    def weight_as_list(self):
        return self.ingredients_weights.split(",")

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        if not self.slug:
            self.slug = slugify(self.name)
        super(Meals, self).save(*args, **kwargs)

    def get_all_ingredients(self):
        return self.ingredient.all() 

    def __str__(self):
        return self.name

    @property   
    def protein(self):
        return self.ingredient.aggregate(Sum("protein"))["protein__sum"]
        
    @property   
    def carbohydrates(self):
        return self.ingredient.aggregate(Sum("carbohydrates"))["carbohydrates__sum"]

    @property   
    def fat(self):
        return self.ingredient.aggregate(Sum("fat"))["fat__sum"]


    @property 
    def quantity(self):
        return self.ingredient.aggregate(Sum("quantity"))["quantity__sum"]

    @property   
    def diet_category(self):
        #diet_types = ["vegan", "vegeterian", "Keto", "Paleo", "Gluten-free"]
        diet_types = "vegan, vegeterian, Keto, Paleo, Gluten-free"
        food_types = ""
        for ing in self.ingredient.all():
            food_types += ing.food_type
        if "1" in food_types: 
            diet_types = diet_types.replace("vegan, ", "").replace(" vegeterian,", "")
        if "7" in food_types or "4" in  food_types:
            diet_types = diet_types.replace("vegan,", "")
        if "6" in food_types:       
            diet_types = diet_types.replace(" Keto,", "").replace(" Paleo,", "").replace(" Gluten-free", "")
        if "2" in  food_types:          
            diet_types = diet_types.replace(" Keto,", "")   
        return (diet_types + " | " + food_types)        

    def get_absolute_url(self):
        return reverse("meal_desc", kwargs={"pk":self.pk})




    





