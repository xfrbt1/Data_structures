import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab
from graphs import Graph

nodes = [1, 2, 3, 4, 5, 6, 7, 8]
link_list = [[1, 2, 5],
             [1, 4, 10],
             [1, 6, 20],

             [2, 4, 5],
             [2, 6, 15],
             [2, 3, 100],
             [2, 8, 15],

             [3, 5, 15],
             [3, 7, 10],
             [3, 8, 15],

             [4, 6, 35],

             [5, 7, 25],
             [5, 8, 10],

             [6, 7, 5],
             [6, 8, 50],
             ]

graph1 = Graph(nodes)
graph1.create_links(link_list)

graph1.print_all_nodes()
print('\n')
graph1.print_am()
print('\n')
graph1.print_wam()
print('\n')

wm = graph1.weight_adj_matrix()
graph = nx.Graph(np.matrix(wm))
print(nx.maximal_independent_set(graph))


# for i in range(len(wm)):
#     for j in range(len(wm)):
#         if wm[i][j] != 0:
#             graph.add_edge(i, j, weight=wm[i][j])
#
# pos = nx.spring_layout(graph, seed=5)
# nx.draw(graph, pos, with_labels=False, node_size=600)
# nx.draw_networkx_labels(graph, pos, font_size=22, font_family="sans-serif")
#
# edge_labels = dict([((u, v,), d['weight']) for u, v, d in graph.edges(data=True)])
# nx.draw_networkx_edges(
#     graph, pos,  alpha=1, edge_color="b", style="dashed"
# )
# nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
#
# plt.show()




