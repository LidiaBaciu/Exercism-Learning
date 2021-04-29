def to_rna(dna_strand):
    DNA_dic = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna = []
    for i in dna_strand:
        rna.append(DNA_dic[i])
    return ''.join(rna)


