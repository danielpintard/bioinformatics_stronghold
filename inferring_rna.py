freq = {
    'A': 4, 'C': 2, 'D': 2, 'E': 2,
    'F': 2, 'G': 4, 'H': 2, 'I': 3,
    'K': 2, 'L': 6, 'M': 1, 'N': 2,
    'P': 4, 'Q': 2, 'R': 6, 'S': 6,
    'T': 4, 'V': 4, 'W': 1, 'Y': 2,
    'Stop': 3
}

data = open('/Users/danielpintard/Downloads/rosalind_mrna (1).txt', 'r').read().strip()

def possible_sequences(sequence):
    aa_freq = freq
    n = aa_freq['Stop']
    for i in sequence:
        n *= aa_freq[i]  
    return n % 1000000
        
print(possible_sequences(data))