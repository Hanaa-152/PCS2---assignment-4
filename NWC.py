import networkx as nx

def neg_cycle(graph):
    try:
        for node in graph.nodes:
            nx.single_source_bellman_ford_path_length(graph, source=node)
        return "-1"
    except nx.NetworkXUnbounded:
        return "1"

file_path = "/Users/han3/Downloads/rosalind_nwc-6.txt"

with open(file_path, "r") as file:
    k = int(file.readline().strip())
    results = []
    for _ in range(k):
        n, m = map(int, file.readline().strip().split())
        graph = nx.DiGraph()
        for _ in range(m):
            u, v, w = map(int, file.readline().strip().split())
            graph.add_edge(u, v, weight=w)
        results.append(neg_cycle(graph))

print(" ".join(results))

