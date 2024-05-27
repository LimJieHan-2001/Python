def read_Genome(lambda_virus.fa):
    genome = ''
    with open(lambda_virus.fa, 'r') as f:
        for line in f:
            if not line.startswith('>'):
                genome += line.rstrip()
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

def reverse_Complement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t

# Reading the genome from the file
genome = read_Genome('lambda_virus.fa')

# Define the pattern and the maximum number of mismatches
pattern = 'AGTCGA'  # Example pattern
max_mismatches = 2  # Example maximum number of mismatches

# Find occurrences in the genome
occurrences = naive_with_mismatches(pattern, genome, max_mismatches)

# Find occurrences in the reverse complement of the genome
reverse_pattern = reverse_Complement(pattern)
reverse_occurrences = naive_with_mismatches(reverse_pattern, genome, max_mismatches)

# Combine occurrences
all_occurrences = occurrences + reverse_occurrences

print("Occurrences:", all_occurrences)
