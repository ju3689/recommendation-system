from Tree_and_methods import TreeNode, bfs
from restaurantData import continents_and_regions, restaurant_data
from LinkedList import Node, LinkedList

def build_tree_structure(continents_and_regions, restaurant_data):
    my_root_node = TreeNode('World')
    for item in continents_and_regions:
        continent = item[0]
        # print("Going through continent: ", continent)
        continent_node = TreeNode(continent)
        my_root_node.add_child(continent_node)
        print("Adding ", continent, " as a new node")
        list_region = item[1]
        print(str(my_root_node))

        #adding child nodes to the tree which will be regions and type of cuisine
        for region in list_region:
            region_node = TreeNode(region)
            continent_node.add_child(region_node)
            print("Adding ", region, " as a new node to ", continent_node.value)        
            food_type_region = [x[2] for x in restaurant_data if x[1] == region]
            food_type_region = list(set(food_type_region))
            for type_food in food_type_region:
                food_type_node = TreeNode(type_food)
                region_node.add_child(food_type_node)
                #creating a linkedlist of all the restaurants matching that type of cuisine
                rest_llist = LinkedList()
                restaurants = [x for x in restaurant_data if x[2] == type_food]

                for item in restaurants:
                    #print("Adding ", item[3], "to the linkedlist for ", item[2], "food to ", str(region_node.value))
                    rest_llist.insert_beginning(item[3:])
                rest_node = TreeNode(rest_llist)
                food_type_node.add_child(rest_node)
    
    return my_root_node

