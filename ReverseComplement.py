from Bio import SeqIO

def find_offset(genome, sequence):
    offset = genome.find(sequence)
    offset_rc = genome.find(sequence.reverse_complement())
    return min(offset, offset_rc)

# Load the genome
genome = SeqIO.read("lambda_virus.fa", "fasta").seq

# Find the offset
offset = find_offset(genome, "ATGCAGT")

print(f"The offset of the leftmost occurrence of 'ATGCAGT' or its reverse complement in the lambda virus genome is {offset}.")
