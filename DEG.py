file_path = "/Users/han3/Downloads/rosalind_deg.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

n, m = map(int, lines[0].strip().split())

degree = [0] * n

for line in lines[1:]:
    u, v = map(int, line.strip().split())
    degree[u - 1] += 1
    degree[v - 1] += 1

print(" ".join(map(str, degree)))
