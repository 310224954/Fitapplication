from django.test import TestCase
from datetime import date
#from Food.models import Products
import json



with open("C:/Users/User/Desktop/Django/FitApp/Main/files/products.json") as input:
	prod_json = json.load(input)



with open("files/products.json") as input:
	prod_json = json.load(input)

for i in prod_json:
	prod = Products(name=i['Name'],	protein=i['Protein'], carbohydrates=i['Carbohydrates'], fat=i['Fat'], description=i['Description'], quantity=i['Quantity'], price=i['Price'], food_type=i['Food type'], slug=i['slug'])                               
	prod.save()





x = sum([i for i in range(5)])
y = sum([i for i in range(5)])
z = sum([i for i in range(5)])

a = sum([x,y,z])

print(a)









