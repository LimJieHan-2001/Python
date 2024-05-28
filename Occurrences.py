from Bio import SeqIO

def count_sequence(genome, sequence):
    return genome.count(sequence) + genome.count(sequence.reverse_complement())

# Load the genome
genome = SeqIO.read("lambda_virus.fa", "fasta").seq

# Count the occurrences
count = count_sequence(genome, "AACT")

print(f"The sequence 'AACT' or its reverse complement occurs {count} times in the lambda virus genome.")
