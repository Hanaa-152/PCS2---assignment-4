import networkx as nx
file_path = "/Users/han3/Downloads/rosalind_bf.txt"

with open(file_path, "r") as file:
    n, m = map(int, file.readline().split())
    graph = nx.DiGraph()
    graph.add_nodes_from(range(1, n + 1))  
    for line in file:
        u, v, w = map(int, line.split())
        graph.add_edge(u, v, weight=w)

try:
    distances = nx.single_source_bellman_ford_path_length(graph, 1)
    print(" ".join(str(distances.get(i, "x")) for i in range(1, n + 1)))
except nx.NetworkXUnbounded:
    print("The graph contains a negative weight cycle.")


