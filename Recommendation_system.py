from restaurantData import types, restaurant_data

# for item in types:
#     print(item)

user_food_pref = "aus"
lg = len(user_food_pref)

possible_food_choices = [x for x in types if user_food_pref in x[:lg]]

print(possible_food_choices)


