import networkx as nx

file_path = "/Users/han3/Downloads/rosalind_sdag-2.txt"

with open(file_path, "r") as file:
    n, m = map(int, file.readline().split())
    graph = nx.DiGraph()
    for _ in range(m):
        u, v, w = map(int, file.readline().split())
        graph.add_edge(u, v, weight=w)

distances = ["x"] * (n + 1)
distances[1] = 0

if nx.is_directed_acyclic_graph(graph):
    for node in nx.topological_sort(graph):
        if distances[node] != "x":
            for neighbor in graph.successors(node):
                weight = graph[node][neighbor]["weight"]
                if distances[neighbor] == "x" or distances[neighbor] > distances[node] + weight:
                    distances[neighbor] = distances[node] + weight

print(" ".join(str(distances[i]) for i in range(1, n + 1)))
