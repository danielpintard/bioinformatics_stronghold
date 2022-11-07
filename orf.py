import re 
from Bio import SeqIO

#grab data set file and process it to yeild the sequence
record = SeqIO.read("/Users/danielpintard/downloads/rosalind_orf (2).txt", 'fasta')
string = record.seq
#then trancribe sequence into RNA sequence
rna_seq = str(string.replace('T', 'U'))
#then get reverse complementary strand by reversing the RNA string and then swasping out the bases for their base compliments
reverse_comp = (rna_seq[::-1].replace("A", "u").replace("U", "a").replace("G", "c").replace('C', 'g')).upper()

amino_acid_codon_dict = {'UUU':'F', 'UUC':'F', 'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', 'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 'UAU':'Y', 'UAC':'Y', 'UAA':'Stop', 'UAG':'Stop', 'UGU':'C', 'UGC':'C', 'UGA':'Stop', 'UGG':'W', 
                   'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'CAU':'H','CAC':'H', 'CAA':'Q','CAG':'Q','CGU':'R','CGC':'R','CGA':'R','CGG':'R',
                   'AUU':'I', 'AUC':'I','AUA':'I','AUG':'M','ACU':'T','ACC':'T','ACA':'T','ACG':'T','AAU':'N','AAC':'N','AAA':'K','AAG':'K','AGU':'S','AGC':'S','AGA':'R','AGG':'R','GUU':'V','GUC':'V',
                   'GUA':'V','GUG':'V','GCU':'A','GCC':'A','GCA':'A','GCG':'A','GAU':'D','GAC':'D','GAA':'E','GAG':'E','GGU':'G','GGC':'G','GGA':'G','GGG':'G'}

#reg expression patter to search the strings for reading frames that start with 'AUG' and end with stop codons(UAA, UAG, UGA)
pattern = re.compile(r'(?=(AUG(?:...)*?)(?=UAA|UAG|UGA))')
#function that searches through the RNA sequence and the reverse compliment for reading frames
frags = []
for s in re.findall(pattern, rna_seq):
    frags.append(s)
for s in re.findall(pattern, reverse_comp):
    frags.append(s)

#function that translates the orf fragments into protein sequences 
translations = []
for sequence in frags:
    split_codons = [] #
    prot_seq = []
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        split_codons.append(codon)
    for s in split_codons: 
        prot_seq.append(amino_acid_codon_dict[s])
    for i in prot_seq: 
        translations.append(''.join(prot_seq))
        break
    
#the list "translations" is looped through to get rid of duplicate sequences and then return the answer 
answer = []
[answer.append(x) for x in translations if x not in answer] 
print('\n'.join(answer))

        


        
    


        
    



    
    
    
    
        



