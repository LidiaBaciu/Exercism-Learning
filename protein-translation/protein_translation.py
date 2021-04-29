
CODON_PROTEIN_PAIRS = {
    "AUG" : "Methionine",
    "UUU" : "Phenylalanine",
    "UUC" : "Phenylalanine",
    "UUA" : "Leucine",
    "UUG" : "Leucine",
    "UCU" : "Serine",
    "UCC" : "Serine",
    "UCA" : "Serine",
    "UCG" : "Serine",
    "UAU" : "Tyrosine",
    "UAC" : "Tyrosine",
    "UGU" : "Cysteine",
    "UGC" : "Cysteine",
    "UGG" : "Tryptophan",
    "UAA" : "STOP",
    "UAG" : "STOP",
    "UGA" : "STOP",
}

def proteins(strand):
    sequence = []
    length = len(strand)
    i = 0
    while(i < length):
        codon = strand[i : (i+3)]
        protein = CODON_PROTEIN_PAIRS[codon]
        if protein == 'STOP':
            break
        sequence.append(protein)
        i = i + 3
    return sequence

