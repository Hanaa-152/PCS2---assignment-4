import networkx as nx

def shortest_cycle(graph, edge):
    u, v = edge[:2]  
    weight = graph[u][v]['weight']
    graph.remove_edge(u, v)
    try:
        path_length = nx.shortest_path_length(graph, source=v, target=u, weight='weight')
        return path_length + weight
    except nx.NetworkXNoPath:
        return -1
    finally:
        graph.add_edge(u, v, weight=weight)

file_path = "/Users/han3/Downloads/rosalind_cte-5.txt"

with open(file_path, "r") as file:
    k = int(file.readline().strip())
    results = []
    for _ in range(k):
        n, m = map(int, file.readline().strip().split())
        graph = nx.DiGraph()
        edges = [tuple(map(int, file.readline().strip().split())) for _ in range(m)]
        for u, v, w in edges:
            graph.add_edge(u, v, weight=w)
        results.append(shortest_cycle(graph, edges[0]))

print(" ".join(map(str, results)))
