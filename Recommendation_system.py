from restaurantData import types, restaurant_data

# for item in types:
#     print(item)


def autocomplete(food_pref, list_options):

    #lg = len(food_pref)
    possible_food_choices = [x for x in list_options if food_pref in x]
    print("Possible food choices are ", ", ".join(possible_food_choices))
    return possible_food_choices


user_food_pref = "korea"
suggestions_list = autocomplete(user_food_pref,types)
print(suggestions_list)
if not ((user_food_pref in types) and (len(suggestions_list) == 1)):
    while suggestions_list:
        print("Oops, it looks like we do not have such cuisine around, did you mean: {0}".format(", ".join(suggestions_list)))
        user_food_pref= input("?\n")
        if user_food_pref in types:
            break
        else:
            suggestions_list = autocomplete(user_food_pref,types)

valid_pref = user_food_pref