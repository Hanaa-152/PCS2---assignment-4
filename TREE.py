file_path = "/Users/han3/Downloads/rosalind_tree.txt" 

with open(file_path, "r") as file:
    dataset = file.readlines()

n = int(dataset[0].strip())  
edges_count = len(dataset[1:]) 
print(n - edges_count - 1)
