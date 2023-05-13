from Tree_and_methods import TreeNode, bfs
from restaurantData import continents_and_regions, restaurant_data

def build_tree_structure(continents_and_regions, restaurant_data):
    my_tree = TreeNode('World')
    for item in continents_and_regions:
        continent = item[0]
        continent_node = TreeNode(continent)
        continent_node = my_tree.add_child(continent)
        list_region = item[1]
        for region in list_region:
            region_node = TreeNode(region)
            continent_node.add_child(region_node)
            restaurant_in_that_region = [x for x in restaurant_data if x[1] == region]
            #then add the linked list for each restaurant --> prior to that add a LinkedList module


