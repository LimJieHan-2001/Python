from Bio import SeqIO
from Bio.Seq import Seq

def count_sequence(genome, sequence):
    sequence = Seq(sequence)  # Convert to Biopython Seq object
    return genome.count(sequence) + genome.count(sequence.reverse_complement())

def read_genome(file_path):
    genome = SeqIO.read(file_path, "fasta").seq
    return genome

def naive_with_mismatches(p, t, max_mismatches):
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        mismatches = 0
        for j in range(len(p)):
            if t[i + j] != p[j]:
                mismatches += 1
                if mismatches > max_mismatches:
                    break
        if mismatches <= max_mismatches:
            occurrences.append(i)
    return occurrences

def find_offset(genome, sequence):
    sequence = Seq(sequence)
    offset = genome.find(sequence)
    offset_rc = genome.find(sequence.reverse_complement())
    if offset == -1:  # If the sequence is not found
        return offset_rc
    if offset_rc == -1:  # If the reverse complement is not found
        return offset
    return min(offset, offset_rc)

# Load the genome
genome = read_genome("lambda_virus.fa")

# Count the occurrences
sequence = "AACT"
count = count_sequence(genome, sequence)
print(f"The sequence '{sequence}' or its reverse complement occurs {count} times in the lambda virus genome.")

# Define the pattern and the maximum number of mismatches
pattern = 'AGTCGA'  # Example pattern
max_mismatches = 2  # Example maximum number of mismatches

# Find occurrences in the genome
occurrences = naive_with_mismatches(pattern, genome, max_mismatches)

# Find occurrences in the reverse complement of the genome
reverse_pattern = str(Seq(pattern).reverse_complement())
reverse_occurrences = naive_with_mismatches(reverse_pattern, genome, max_mismatches)

# Combine occurrences
all_occurrences = occurrences + reverse_occurrences
print("Occurrences:", all_occurrences)

# Find the offset
sequence = "ATGCAGT"
offset = find_offset(genome, sequence)
print(f"The offset of the leftmost occurrence of '{sequence}' or its reverse complement in the lambda virus genome is {offset}.")
