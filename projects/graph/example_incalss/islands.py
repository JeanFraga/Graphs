# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4


# islands consist of - connected components
# connected - neighbors(edges)
# directions, new (edges)
# 2d array - graph, more or less?
# returns(shape of solution) - number of islands

# How could we write a get neighbor function that uses this shape?
# Offset coordinates

# How can we find the extent of an island?
# Either of our traversals to find all of the nodes in an island

# How do I explore the larger set?
# Loop through and call a traversal if we find an unvisited 1
def get_neighbors(row, col):
    neighbor_list = []
    if islands[row][col+1] == 1:
        neighbor_list.append((row, col+1))

def island_counter(islands):
    counter = 0
    visited = set()

    # column loop:
    for row in range(len(islands)-1):
        for column in range(len(islands[row])-1):
            print('islands in each index', islands[row][column])

            if islands[row][column] == 1:
                if (row,column) not in visited:
                    visited.add((row, column))
                    counter +=1


island_counter(islands)