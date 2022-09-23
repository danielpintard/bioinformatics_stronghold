#code does not work - Update: code works, I just had to fix the function responsible for getting the sequence names and strings to account for \n in the data 
# data = open('grph_samdata.txt', 'r').read()
data = open('/Users/danielpintard/Downloads/rosalind_grph (1).txt', 'r').read()


k = 3
#manage fasta format 
if '>' in data :
    data_array = data.split('>')
    for i in data_array: 
        if i == '': data_array.remove(i)
    for i in data_array: data_array[data_array.index(i)] = i.split('\n', 1)
    for i in data_array: data_array[data_array.index(i)] = [i[0], i[1].replace('\n', '')]
    print(data_array)
   
data_dict = {}
for i in data_array: 
    indiv_seq = data_array[data_array.index(i)]
    for j in indiv_seq: 
        data_dict[indiv_seq[0]] = indiv_seq[1]


#find overlap - does not work 
for seq in data_dict: 
    for seq2 in data_dict: 
        key, value = seq, data_dict[seq] 
        key2, value2 = seq2, data_dict[seq2]
        if seq == seq2:
            continue 
        suffix = data_dict[seq][-k:] 
        prefix = data_dict[seq2][:k]
        if prefix == suffix: 
            print(seq, seq2)