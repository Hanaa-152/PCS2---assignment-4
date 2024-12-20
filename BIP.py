import networkx as nx

file_path = "/Users/han3/Downloads/rosalind_bip.txt"

with open(file_path, "r") as file:
    k = int(file.readline().strip())
    results = []
    for _ in range(k):
        while True:  
            line = file.readline().strip()
            if line:
                break

        num_vertices, num_edges = map(int, line.split())
        graph = nx.Graph()
        for _ in range(num_edges):
            u, v = map(int, file.readline().split())
            graph.add_edge(u, v)

        if nx.is_bipartite(graph):
            results.append("1")
        else:
            results.append("-1")

print(" ".join(results))
