import networkx as nx
file_path = "/Users/han3/Downloads/rosalind_dag.txt"

with open(file_path, "r") as file:
    k = int(file.readline().strip())
    results = []
    for _ in range(k):
        line = file.readline().strip()
        while not line:
            line = file.readline().strip()
        
        num_vertices, num_edges = map(int, line.split())
        graph = nx.DiGraph()
        for _ in range(num_edges):
            edge_line = file.readline().strip()
            if edge_line:  
                u, v = map(int, edge_line.split())
                graph.add_edge(u, v)
        
        results.append(1 * nx.is_directed_acyclic_graph(graph) or -1)

print(" ".join(map(str, results)))
