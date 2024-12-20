file_path = "/Users/han3/Downloads/rosalind_bfs.txt"

with open(file_path, "r") as file:
    num_vertices, num_edges = map(int, file.readline().split())
    graph = {i: [] for i in range(1, num_vertices + 1)}
    for line in file:
        start, end = map(int, line.split())
        graph[start].append(end)

distances = [-1] * (num_vertices + 1)
distances[1] = 0

queue = [1]
while queue:
    current = queue.pop(0)
    for neighbor in graph[current]:
        if distances[neighbor] == -1:
            distances[neighbor] = distances[current] + 1
            queue.append(neighbor)

print(" ".join(map(str, distances[1:])))
