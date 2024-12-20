file_path = "/Users/han3/Downloads/rosalind_ddeg.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

n, m = map(int, lines[0].strip().split())
edges = [tuple(map(int, line.strip().split())) for line in lines[1:]]

degree = [0] * n
adjacency_list = [[] for _ in range(n)]

for u, v in edges:
    degree[u - 1] += 1
    degree[v - 1] += 1
    adjacency_list[u - 1].append(v - 1)
    adjacency_list[v - 1].append(u - 1)

neighbor_degree_sum = [0] * n

for i in range(n):
    neighbor_degree_sum[i] = sum(degree[neighbor] for neighbor in adjacency_list[i])

print(" ".join(map(str, neighbor_degree_sum)))
