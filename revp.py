from Bio import SeqIO

record = SeqIO.read('/Users/danielpintard/downloads/rosalind_revp (1).txt', 'fasta')

dna = str(record.seq)
comp = str(record.seq.complement())

for i in range(len(dna)):
    for j in range(len(comp)):
        frag = dna[i : j + 1]
        r_frag = comp[i : j + 1]
        if len(frag) >=4 and len(frag) <= 12:
            if frag == r_frag[::-1]:
                print( i+1, len(frag))


#looping through the range of the length of dna string, 
# and 'simultaneously' looping through the range of the 
# length of the complement string

#then indexing a fragment in the range of the length of dna string
# and matching that index with that of the complement string
# 
        