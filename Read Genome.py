def readGenome(lambda_virus.fa):
    genome = ''
    with open(lambda_virus.fa, 'r') as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome
