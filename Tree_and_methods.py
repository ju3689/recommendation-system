from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child_node):
        #creates parent-child relationship
        self.children.append(child_node)
        # print("Added ", child_node.value, " to ", self.value)

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
    
    def __str__(self):
        stack = deque()
        stack.append([self, 0])
        level_str = "\n"
        while len(stack) > 0:
            node, level = stack.pop()
            if level > 0:
                level_str += "| "*(level-1)+ "|-"
            level_str += str(node.value)
            level_str += "\n"
            level+=1
            for child in reversed(node.children):
                stack.append([child, level])
        return level_str


def bfs(root_node, goal_value):
  # Initialize a queue and a set to keep track of visited nodes.
  queue = [(root_node, [])]
  visited = set()

  # While the queue is not empty, do the following:
  while queue:
    # Pop the first node and path from the queue.
    node, path = queue.pop(0)

    # If the node is the goal node, return the path.
    if node.value == goal_value:
      return node

    # Otherwise, mark the node as visited and add its children to the queue.
    visited.add(node)
    for child in node.children:
      if child not in visited:
        queue.append((child, path + [node]))

  # If the queue is empty and the goal node is not found, return None.
  return None