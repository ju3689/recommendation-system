from restaurantData import types, restaurant_data

# for item in types:
#     print(item)


def autocomplete(food_pref, list_options):

    lg = len(food_pref)
    possible_food_choices = [x for x in list_options if food_pref in x[:lg]]
    return possible_food_choices


user_food_pref = "aus"

if user_food_pref not in types:
    suggestions_list = autocomplete(user_food_pref,types)
    while suggestions_list:
        print("Oops, it looks like we do not have such cuisine around, did you mean: {0}".format(", ".join(suggestions_list)))
        user_food_pref= input("?")
        if user_food_pref in types:
            break
        else:
            suggestions_list = autocomplete(user_food_pref,types)

valid_pref = user_food_pref