# Enter your code here. Read input from STDIN. Print output to STDOUT
graph = input()

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def print_node(self):
        print("value: {}, children: {}".format(self.value, self.children))
        
def create_graph(inp):
    stack = []
    root = None
    node_count = 0
    for char in inp:
        if char == '(':  
            new_node = Node(node_count)
            node_count += 1
            if stack:
                parent = stack[-1]
                parent.children.append(new_node)
            else:
                root = new_node

            stack.append(new_node)

        elif char == ')':
            stack.pop()

    return root
    
def find_max_depth(node, current_depth=0):
    if not node:
        return current_depth
        
    node.print_node()
    depths = [find_max_depth(child, current_depth + 1) for child in node.children]
    return max(depths)

#used for debugging
def print_graph(node, depth=0):
    if node:
        print('  ' * depth + str(node.value))
        for child in node.children:
            print_graph(child, depth + 1)
            

    
root = create_graph(graph)
print_graph(root)
print("pPPPPPPP")
print(root.children)
print(find_max_depth(root))

print(graph)

#((()((()())))()(()))