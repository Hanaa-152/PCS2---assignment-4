import re

file_path = "/Users/han3/Downloads/rosalind_long-2.txt"  

with open(file_path, "r") as file:
    dataset = file.read()

sequences = re.findall(r'[ATGC]+', dataset)
names = re.findall(r'Rosalind_[0-9]+', dataset)

while len(sequences) > 1:
    max_overlap = 0
    merge_a, merge_b = 0, 0
    for i in range(len(sequences)):
        for j in range(len(sequences)):
            if i != j:
                for k in range(len(sequences[i]) // 2, len(sequences[i])):
                    suffix = sequences[i][-k:]
                    prefix = sequences[j][:k]
                    if suffix == prefix and k > max_overlap:
                        max_overlap = k
                        merge_a, merge_b = i, j

    sequences[merge_a] += sequences[merge_b][max_overlap:]
    sequences.pop(merge_b)

print(sequences[0])
