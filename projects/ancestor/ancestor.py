from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for i in ancestors:
        graph.add_vertex(i[0])
        graph.add_vertex(i[1])
        # graph.add_edge(i[1], i[0])
    # this order lets me see the parents of every number
    # {1: {3}, 3: {6}, 2: {3}, 6: set(), 5: {6, 7}, 7: set(), 4: {8, 5}, 8: {9}, 9: set(), 11: {8}, 10: {1}}
    for i in ancestors:
        graph.add_edge(i[1], i[0])
    # print(graph.vertices)
    answer = graph.bft(starting_node)
    if answer == starting_node:
        return -1
    else:
        return answer



# print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 6))