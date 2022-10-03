import sys
import requests 

with open('/Users/danielpintard/Downloads/rosalind_mprt (5).txt', 'r') as data:
    accession_values = data.read().replace('\n', ' ').split()
    for i in accession_values: accession_values[accession_values.index(i)] = i.split('_')
    for i in accession_values: accession_values[accession_values.index(i)] = i[0]

url = 'http://www.uniprot.org/uniprot/'
prot_seq = {}
for a_value in accession_values:
    access_url = url + a_value +'.fasta'
    response = requests.get(access_url)
    prot_seq[a_value] = (response.text.split('\n'))
    prot_seq[a_value] = ''.join(prot_seq[a_value][1::])
    

def N_glycosylation_motif(ID, sequence):
    sequence = list(sequence)  
    global result
    result = []
    for i in range(0, len(sequence)-3):
        seq = sequence[i:i+4]
        if (seq[0] == 'N') and (seq[2] == 'S' or seq[2] == 'T') and (seq[1] and seq[3] != 'P') : 
            result.append(i+1) 
    

for key, value in prot_seq.items():
    N_glycosylation_motif(key, value)
    if not result: 
        continue 
    else: 
        print(key)
        print(*result)



        
        
        
    


    
