from path_finder import *

# create and qprint map
map_size = 10
nodes = []
print_text = "  Map:\n   "
for x in range(0, map_size):
    print_text = print_text + " " + str(x) + " "
    
for x in range(0, map_size):
    print_text = print_text + "\n " + str(x) +  "|"
    for y in range(0, map_size):
        nodes.append(Node(x, y))
        print_text = print_text+" + "

print(print_text)

# finder
finder = PathFinder(nodes)
finder.findPath(nodes[0], nodes[64])


# show path
print_text = "  Path:\n   "
for x in range(0, map_size):
    print_text = print_text + " " + str(x) + " "

for x in range(0, map_size):
    print_text = print_text + "\n " + str(x) +  "|"
    for y in range(0, map_size):
        found = False
        for node in finder.path:
            if(node.x == x and node.y == y):
                print_text = print_text + " o "
                found = True
                break             
        if(not found):
            print_text = print_text + " + "
           
print(print_text)
