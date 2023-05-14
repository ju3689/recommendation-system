from restaurantData import restaurant_data, continents_and_regions, types_dict
from Tree_and_methods import TreeNode, bfs
from tree_builder import build_tree_structure
from LinkedList import LinkedList

#autocomplete function that will take a user input and try to match it to an existing cuisine
def autocomplete_list(food_pref, list_options):

    #storing possible food choices that contains the string entered by the user
    possible_food_choices = [k for k, v in list_options.items() if food_pref in k]
    return possible_food_choices

#handling inputs from the users
def handle_input_and_choices(food_pref, list_options):
    #collecting all matching cuisine in a list
    suggestions_list = autocomplete_list(food_pref, list_options)
    valid_choice = False
    #if the user input already matches exactly a cuisine we have in our reference table, then the user choice is valid
    if food_pref in list_options: valid_choice = True

    #if user input is perfect match and only 1 cuisine is returned by our autocomplete list, then it's a no brainer
    if len(suggestions_list) == 1 and valid_choice == True: return food_pref

    #if the user input is not valid, then we need to go through some use cases
    #if there is only 1 cuisine that contains the string entered by the user, we want to check if the user meant that one
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
    #if there are more than 1 cuisine matching, we list them all and ask the user to input specifically the one they want
    elif len(suggestions_list) > 1:
        food_pref=input("We have a few options for that ..! Which one specifically do you fancy ? : {0} \n".format(", ".join(suggestions_list)))
        return handle_input_and_choices(food_pref, list_options)
    #if no matches are found, we'll prompt the user to try another type of cuisine
    else:
        food_pref = input("Tough one ... we do not have such type of cuisine around, try something else.\n")
        return handle_input_and_choices(food_pref, list_options) 

    return food_pref

#purpose is to store in a dictionary only the restaurants serving that type of food
def display_results(node_data):
    nodes = node_data.children
    lst_version = ""
    for node in nodes:
        node.value.stringify_list()


    #str_results = rest_node.stringify_list()
    #return str_results

#displaying the list of restaurants nicely
# def display_results(shortlist_rest):
#     for k, v in shortlist_rest.items():



print("Welcome to our restaurant finder service!")
user_food_pref = input("What type of food do you fancy today ?\n")
valid_food_pref = handle_input_and_choices(user_food_pref, types_dict)
print("Got you! We're searching for {0} restaurants now... hang tight!".format(valid_food_pref))

#phase 2: call API

#create Tree made of continent, regions and LinkedList or dictionaries
rest_tree = build_tree_structure(continents_and_regions, restaurant_data)
print(str(rest_tree))

continent_node = bfs(rest_tree, types_dict[valid_food_pref][0])
region_node = bfs(continent_node, types_dict[valid_food_pref][1])
cuisine_node = bfs(region_node, valid_food_pref)

if cuisine_node:
    print("Here are the options you can consider for ", str(valid_food_pref), " food:\n")
    display_results(cuisine_node)
else:
    print("No restaurant matching your criteria unfortunately, please try another cuisine!")
#print(my_results)

# if len(my_hash_table) ==1:
#     print("Here is the only option around for ", str(valid_food_pref), " food:\n")
#     display_results(my_hash_table)
# elif len(my_hash_table) > 1:
#     display_results(my_hash_table)    
# else:
