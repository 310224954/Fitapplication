from django.test import TestCase
import os


# ingredients_weights = "200,150,100,15,40"#[3, 7, 11, 15]
# to_be_deleted = 4
# # print(ingredients_weights.count(","))#4
# coma_positions =[]
# for i in range(len(ingredients_weights)):
# 	if ingredients_weights[i] ==",":
# 		coma_positions.append(i)

# if to_be_deleted == 0:
# 	ingredients_weights = ingredients_weights[coma_positions[to_be_deleted]+1:]
# elif to_be_deleted == len(coma_positions):
# 	ingredients_weights = ingredients_weights[:coma_positions[to_be_deleted-1]]
# else:
# 	ingredients_weights = ingredients_weights[:coma_positions[to_be_deleted-1]] + ingredients_weights[coma_positions[to_be_deleted]:]

# print(ingredients_weights)




# for i, prod in enumerate(meal.get_all_ingredients()):
#     if prod == product:
#         temporary_weights = meal.ingredients_weights
#         temporary_list = temporary_weights.split(",")
#         del temporary_list[i]
#         temporary_weights =""
#         for weight in temporary_list:
#             temporary_weights += weight +","    
#         meal.ingredients_weights = temporary_weights[0:-1]
#         meal.save()  

ingredients_weights = "200,180,100,150"
new = "45"
to_be_changed = 3
coma_positions =[]
for i in range(len(ingredients_weights)):
 	if ingredients_weights[i] ==",":
 		coma_positions.append(i)


if to_be_changed == 0:
	ingredients_weights =  new + "," + ingredients_weights[coma_positions[to_be_changed]+1:]
elif to_be_changed == len(coma_positions):
	ingredients_weights = ingredients_weights[:coma_positions[to_be_changed-1]] + "," + new
else:
	ingredients_weights = ingredients_weights[:coma_positions[to_be_changed-1]] + "," + new +  ingredients_weights[coma_positions[to_be_changed]:]

print(ingredients_weights)