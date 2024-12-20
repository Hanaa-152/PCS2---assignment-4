import networkx as nx
file_path = "/Users/han3/Downloads/rosalind_dij.txt"
with open(file_path, "r") as file:
    num_vertices, num_edges = map(int, file.readline().split())
    graph = nx.DiGraph()
    for line in file:
        u, v, weight = map(int, line.split())
        graph.add_edge(u, v, weight=weight)

distances = [-1] * (num_vertices + 1)
shortest_paths = nx.single_source_dijkstra_path_length(graph, 1)

for node in range(1, num_vertices + 1):
    distances[node] = shortest_paths.get(node, -1)

print(" ".join(map(str, distances[1:])))

