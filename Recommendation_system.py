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

    print(len(suggestions_list))
    print(valid_choice)

    if len(suggestions_list) == 1 and valid_choice == True: return food_pref

    if len(suggestions_list) == 1:
        user_confirm_choice =input("One more effort, did you mean: {0} ? Type \"Yes\" or \"No\" \n".format(", ".join(suggestions_list)))
        if user_confirm_choice == "Yes":
            food_pref = suggestions_list[0]
        elif user_confirm_choice == "No":
            food_pref = input("Ok let's try again. What type of food do you fancy eating ?\n")
            return handle_input_and_choices(food_pref, list_options)
        else:
            food_pref = input("Hmm does not seem like a valid input, let's try again. What type of food do you fancy eating ?\n")
            return handle_input_and_choices(food_pref, list_options)
    elif len(suggestions_list) > 1:
        food_pref=input("We have a few options for that ..! Which one specifically do you fancy ? : {0} \n".format(", ".join(suggestions_list)))
        return handle_input_and_choices(food_pref, list_options)
    else:
        food_pref = input("Tough one ... we do not have such type of cuisine around, try something else.\n")
        return handle_input_and_choices(food_pref, list_options) 

    return food_pref

def store_data_in_hasmap(table_data):
    my_hash_map = {}
    for item in table_data:
        cuisine = item[0]
        rest_name = item[1]
        price_rest = item[2]
        rating_rest = item[3]
        address_rest = item[4]
        my_hash_map[rest_name] = [cuisine, price_rest, rating_rest, address_rest]
    return my_hash_map
    # print(my_hash_map.keys())

def display_results(food_pref, hash_map):
    shortlist_rest = {}
    shortlist_rest = {k: v for k, v in hash_map.items() if v[0] == food_pref}
    for k, v in shortlist_rest.items():
        print("---------------\n")
        print("Restaurant name: {0} \n".format(str(k)))
        print("Price: {0}/5 \n".format(str(v[1])))
        print("Rating: {0}/5 \n".format(str(v[2])))
        print("Address: {0} \n".format(str(v[3])))


print("Welcome to our restaurant finder service!")
user_food_pref = input("What type of food do you fancy today ?\n")
valid_food_pref = handle_input_and_choices(user_food_pref, types)
print("Got you! We're searching for {0} restaurants now... hang tight!".format(valid_food_pref))
my_hash_table = store_data_in_hasmap(restaurant_data)
if len(my_hash_table) ==1:
    print("Here is the only option around for ", str(valid_food_pref), " food:\n")
    display_results(valid_food_pref, my_hash_table)
elif len(my_hash_table) > 1:
    print("Here are the options you can consider for ", str(valid_food_pref), " food:\n")
    display_results(valid_food_pref, my_hash_table)    
else:
    print("No restaurant matching your criteria unfortunately, please try another cuisine!")