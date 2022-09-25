# not outputting correct answer 
data = open('/Users/danielpintard/Downloads/rosalind_lcsm (3).txt', 'r').read()
# data = open('shared_motif_samdata.txt', 'r').read()

if ">" in data: 
    data_array = data.split('>') 
    for i in data_array: 
        if i == '' : data_array.remove(i)
    for i in data_array: data_array[data_array.index(i)] = i.split('\n', 1)
    for i in data_array: data_array[data_array.index(i)] = [i[0], i[1].replace('\n', '')]


sequences = []
for i in data_array:
    i = data_array[data_array.index(i)][1]
    sequences.append(i)

    
sorted_sequences = sorted(sequences, key=len)
shrt_seq = sorted_sequences[0]
comparing_seq = sorted_sequences[1:]
motif = ''
for i in range(len(shrt_seq)):
    for s in range(i, len(shrt_seq)): 
        m = shrt_seq[i:s + 1]
        found = False
        for sequences in comparing_seq:
            if m in sequences:
                found = True
            else: 
                found = False
                break 
        if found and len(m) > len(motif):
            motif = m 
        
print(motif)
                
    
    

    