#Step 1 - Step 1 - have DNA string and its reverse complement
from gettext import find
import re 

string = "GCCTATAAATTCTTCTGTTGTAGGGCCATTCGGAAGCAAGGTACAAGGACGCGATCTGTGGCTTTATACATAAGAATAGCCCTCTGAGACAGTATGCTACATGCGCCAGGTTCTCTTTAATTACCACTTCCACCACTTTCCTGGCTGTGATATCACTCTATGTCATTACGTTCCTTTATCGCATAGATCCATAGATACGATTATCAGTAGCCTCTTAAGTAGATTGTCAACCTCTCTGGGGTCCTTCTTGTGTACGGACCCACCACCGCATCATAACCCGTCTCTGTTAGGAGGGCCCGGAAAACGCATGGTGGTTTATGGGTTACCTCGGAGGCGTAGATTTTTTGCAAAAAAAATATTATTTTGAGCGTGGGCTGCTGAAGAAATGAATTTTCAGTAGATTGTATTGTACGACTGGTTCACAGTTGATTCCGCGCGCACCTTGCGAATGAGGCAGCGAGGATCGGCCGAAAATCATGTTTCCCAAAGTTTTGGTTTAGCTAAACCAAAACTTTGGGAAACATAAGCCACATCAGTGTGACCCTCTCTCATACGTCGATAACGTGACAGATTCGGGTAGATTTGCATTTTCAAAAATATCGCCCTAGTGACCGCGGGACACACGCGGACCTGTCACAGAAACTAATTAGTCTTCACCCGTGACTGACTCTGTGTCGCATGGGCGGCTGTTTTACCATCTTGCAGACCATCTCGGTCACATTTATTACGCCAATTGTACAACCATACAGAAATCGCGTCTCTCTAAACTTCACCTAAGTCAGCATGATGCTTACGATTATAGCTAACACGGTCTTGCGGAATTCGACAAGGCCGTTTAGAGGTCGAGTTTGGGTATGCAGGAGGTTGGGCTCGGCATCAGTGCCTACAGTTTCATCGGTAGTGAAACGACCCTTAGAATTTCAGCAACCATGAAACCCTAGCGGAGGCAACAACCCCTAAAACTAGAGGCGTCGGCCGATGGAAGAGCCTGGGAATTTAA"
rna_seq = string.replace('T', 'U')
reverse_comp = (rna_seq[::-1].replace("A", "u").replace("U", "a").replace("G", "c").replace('C', 'g')).upper()

amino_acid_codon_dict = {'UUU':'F', 'UUC':'F', 'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', 'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 'UAU':'Y', 'UAC':'Y', 'UAA':'Stop', 'UAG':'Stop', 'UGU':'C', 'UGC':'C', 'UGA':'Stop', 'UGG':'W', 
                   'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'CAU':'H','CAC':'H', 'CAA':'Q','CAG':'Q','CGU':'R','CGC':'R','CGA':'R','CGG':'R',
                   'AUU':'I', 'AUC':'I','AUA':'I','AUG':'M','ACU':'T','ACC':'T','ACA':'T','ACG':'T','AAU':'N','AAC':'N','AAA':'K','AAG':'K','AGU':'S','AGC':'S','AGA':'R','AGG':'R','GUU':'V','GUC':'V',
                   'GUA':'V','GUG':'V','GCU':'A','GCC':'A','GCA':'A','GCG':'A','GAU':'D','GAC':'D','GAA':'E','GAG':'E','GGU':'G','GGC':'G','GGA':'G','GGG':'G'}

#Step 2 - loop through RNA sequences to find reading frame 

pattern = re.compile(r'(?=(AUG(?:...)*?)(?=UAA|UAG|UGA))')
frags = []
for s in re.findall(pattern, rna_seq):
    frags.append(s)
for s in re.findall(pattern, reverse_comp):
    frags.append(s)

for sequence in frags:
    split_codons = []
    prot_seq = []
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        split_codons.append(codon)
    for s in split_codons: 
        prot_seq.append(amino_acid_codon_dict[s])
    for i in prot_seq: 
        print(''.join(prot_seq))
        break
    
        


        
    


        
    



    
    
    
    
        




