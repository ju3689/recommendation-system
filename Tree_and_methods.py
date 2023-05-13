class TreeNode:
    def __init__(self, value):
        self.value = None
        self.children = []
    
    def add_child(self, child_node):
        #creates parent-child relationship
        self.children.append(child_node)
        print("Added ", child_node.value, " to ", self.value)

    def remove_child(self, child_node):
        #removes parent-child relationship
        self.children = [child for child in self.children if child != child_node]
        print("Removed ", child_node.value, " from ", self.value)
    
    def traverse(self):
        #moves through each node references from self downwards
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children
    