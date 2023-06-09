class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        current_node = self.get_head_node()
        string_list = ""
        while current_node:
            if current_node.get_value() != None:
                print("---------------\n")
                print("Restaurant name: {0} \n".format(current_node.get_value()[0]))
                print("Price: {0}/5 \n".format(current_node.get_value()[1]))
                print("Rating: {0}/5 \n".format(current_node.get_value()[2]))
                print("Address: {0} \n".format(current_node.get_value()[3]))
                #string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        #return string_list
    
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:                
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node
        

