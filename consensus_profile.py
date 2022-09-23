data = open('/Users/danielpintard/Downloads/rosalind_cons (3).txt', 'r').read()
#data = open('consensus_samdata.txt', 'r').read()

#format data in FASTA file to operate on
if '>' in data :
    data_array = data.split('>')
    for i in data_array:
        if i == '':
             data_array.remove(i)
    for i in data_array: data_array[data_array.index(i)] = i.split('\n', 1)
    for i in data_array: data_array[data_array.index(i)] = [i[0], i[1].replace('\n', '')]
    
    
# create profile
prof_sequences = []

for i in data_array:
    data_array[data_array.index(i)] = i[1]
    prof_sequences.append(i[1])
    
n = len(prof_sequences[0])
 
profile_matrix = {
    'A': [0]*n,
    'C': [0]*n,
    'G': [0]*n,
    'T': [0]*n,
    }

for dna in prof_sequences:
    for position, nucleotide in enumerate(dna):
        profile_matrix[nucleotide][position] += 1

#find consensus string 
result = []
for position in range(n):
    max_count = 0
    max_nucleotide = None
    for nucleotide in profile_matrix:
        if profile_matrix[nucleotide][position] > max_count:
            max_count = profile_matrix[nucleotide][position]
            max_nucleotide = nucleotide
    result.append(max_nucleotide)


print(''.join(result))
print('A:', ' '.join(map(str, profile_matrix['A'])))
print('C:', ' '.join(map(str, profile_matrix['C'])))
print('G:', ' '.join(map(str, profile_matrix['G'])))
print('T:', ' '.join(map(str, profile_matrix['T'])))

    
