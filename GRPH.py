from Bio import SeqIO

file_path = "/Users/han3/Downloads/rosalind_grph.txt"  

k = 3

records = list(SeqIO.parse(file_path, "fasta"))


for record1 in records:
    for record2 in records:
        if record1.id != record2.id and str(record1.seq[-k:]) == str(record2.seq[:k]):
            print(record1.id, record2.id)


