from restaurantData import types, restaurant_data

# for item in types:
#     print(item)


def autocomplete_list(food_pref, list_options):

    #lg = len(food_pref)
    possible_food_choices = [x for x in list_options if food_pref in x]
    # print("Possible food choices are ", ", ".join(possible_food_choices))
    return possible_food_choices

def handle_input_and_choices(food_pref, list_options):
    suggestions_list = autocomplete_list(food_pref, list_options)
    valid_choice = False
    if food_pref in list_options: valid_choice = True
    
    if valid_choice:
        if len(suggestions_list) > 1:
            food_pref=input("We have a few options for that ..! Which one specifically do you fancy ? : {0} \n", ", ".join(suggestions_list))
            return handle_input_and_choices(food_pref, list_options)
    else:
        if len(suggestions_list) >= 1:
            food_pref=input("One more effort, did you mean: {0} ? \n".format(", ".join(suggestions_list)))
            return handle_input_and_choices(food_pref, list_options) 
        else:
            food_pref = input("Tough one ... we do not have such type of cuisine around, try something else.\n")
            return handle_input_and_choices(food_pref, list_options) 

    return food_pref

    



user_food_pref = "kore"
valid_food_pref = handle_input_and_choices(user_food_pref, types)
print("Got you! We're searching for {0} food now... hang tight!".format(valid_food_pref))
