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
        if len(suggestions_list) == 1:
            user_confirm_choice =input("One more effort, did you mean: {0} ? Type \"Yes\" or \"No\" \n".format(", ".join(suggestions_list)))
            if user_confirm_choice == "Yes":
                 food_pref = suggestions_list[0]
            elif user_confirm_choice == "No":
                print("Ok let's try again.")
                return handle_input_and_choices(food_pref, list_options)
            else:
                print("Hmm does not seem like a valid input, let's try again")
                return handle_input_and_choices(food_pref, list_options)
        elif len(suggestions_list) > 1:
            #food_pref=input("We have a few options for that ..! Which one specifically do you fancy ? : {0} \n", ", ".join(suggestions_list))
            return handle_input_and_choices(food_pref, list_options)
        else:
            food_pref = input("Tough one ... we do not have such type of cuisine around, try something else.\n")
            return handle_input_and_choices(food_pref, list_options) 

    return food_pref

print("Welcome to our restaurant finder service!")
user_food_pref = input("What type of food do you fancy today ?\n")
valid_food_pref = handle_input_and_choices(user_food_pref, types)
print("Got you! We're searching for {0} restaurants now... hang tight!".format(valid_food_pref))
