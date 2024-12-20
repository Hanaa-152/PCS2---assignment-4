file_path = "/Users/han3/Downloads/rosalind_cc-4.txt"

with open(file_path, "r") as file:
    n, m = map(int, file.readline().split())
    graph = {i: [] for i in range(1, n + 1)}
    for line in file:
        u, v = map(int, line.split())
        graph[u].append(v)
        graph[v].append(u)

def dfs(node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)

visited = [False] * (n + 1)
components = sum(1 for v in range(1, n + 1) if not visited[v] and not dfs(v))
print(components)
