from graphs import Graph

nodes = [1, 2, 3, 4, 5, 6, 7, 8]
link_list = [[1, 2, 1],
             [1, 4, 1],
             [1, 6, 1],

             [2, 4, 1],
             [2, 6, 1],
             [2, 3, 1],
             [2, 8, 1],

             [3, 5, 1],
             [3, 7, 1],
             [3, 8, 1],

             [4, 6, 1],

             [5, 7, 1],
             [5, 8, 1],

             [6, 7, 1],
             [6, 8, 1],
             ]

graph = Graph(nodes)
graph.new_node(9)

graph.create_links(link_list)
graph.print_all_nodes()
m = graph.adj_matrix()
wm = graph.w_adj_matrix()


