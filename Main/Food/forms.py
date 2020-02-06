from django import forms

from .models import Products, Meals


class ProductForm(forms.ModelForm): #forms.Form
    name = forms.CharField(
        widget=forms.TextInput(
            attrs ={
                "placeholder":"Pass here new product name.",
                "size":25,
                "title":"New product name"
                }
            )
        )
    food_type = forms.ChoiceField(choices = (
            ("1", "Meat"),
            ("2", "Fruit"),
            ("3", "Vegetable"), 
            ("4", "SeaFood"),
            ("5", "Nuts"),
            ("6", "Grains"),
            ("7", "Diary")
        )
    )
    protein = forms.FloatField(widget = forms.NumberInput(attrs= {"placeholder":"Protein content."}))
    carbohydrates = forms.FloatField(widget = forms.NumberInput(attrs= {"placeholder":"Carbohydrates content."}))
    fat = forms.FloatField(widget = forms.NumberInput(attrs= {"placeholder":"Fat content."}))
    description = forms.CharField(
        min_length=20, 
        widget=forms.Textarea(
            attrs={
                "placeholder":"Plese enter here product desctipion.",
                "class":"new-form",
                "rows":15,
                "cols":50
            }
        )
    )
    quantity = forms.IntegerField(widget = forms.NumberInput(attrs={"placeholder":"Grams of product per portion.", "size":40}))
    price = forms.DecimalField(initial=0.99)    
    
    class Meta:     
        model = Products                
        fields = ["name", "food_type", "protein", "carbohydrates", "fat", "description", "quantity", "price"]



class MealCreationForm(forms.Form):
    name = forms.CharField(max_length = 50)   
    description = forms.CharField(
        min_length=20, 
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder":"Plese enter here product desctipion.",
                "class":"new-form",
                "rows":8,
                "cols":50
            }
        )
    )
    ingredient = forms.ModelMultipleChoiceField(
        Products.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={}),
    )

    class Meta:
        model = Meals
        fields = ["name", "ingredient", "description"]

class MealUpdateForm(forms.Form):
    description = forms.CharField(
        min_length=20, 
        widget=forms.Textarea(
            attrs={
                "class":"new-form",
                "rows":15,
                "cols":50
            }
        )
    )

    class Meta: 
        model = Meals
        fields = ["description"]


# class MealQuantityUpdate(forms.Form):
#     ingredients_weights = ingredients_weights
    

#     class Meta: 
#         model = Meals
#         fields = ["Weight"]





