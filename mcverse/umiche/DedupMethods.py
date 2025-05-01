import umiche as uc


graph_adj_umitools = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C'],
    'C': ['A', 'B'],
    'D': ['A', 'E', 'F'],
    'E': ['D'],
    'F': ['D'],
}

adj = uc.graph.adjacency(
    graph_adj=graph_adj_umitools,
)
print(adj.graph)


splitter = uc.homotrimer.collapse()
print(splitter.vote('AAA', recur_len=3))
print(splitter.vote('TAA', recur_len=3))
print(splitter.vote('TGA', recur_len=3))