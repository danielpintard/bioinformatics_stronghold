data = open('/Users/danielpintard/Downloads/rosalind_gc (1).txt', 'r').read()
#data = open('gc_samdata.txt', 'r').read()

id_seq = {}
gc_content_dict = {}

#clean up data - distinguish the individual sequences - takes FASTA format, deconstructs into a list of sequences (that contain newlines in seq but not in id just to differentiate them) 
if '>' in data :
    data_array = data.split('>')
    for i in data_array:
       if i == '':
            data_array.remove(i)
    for i in data_array:
        data_array[data_array.index(i)] = i.split('\n', 1)

for i in data_array:
    data_array[data_array.index(i)] = i 
    id = i[0]
    seq = i[1]
    id_seq[id] = seq
    print(id_seq)
    

for id,seq in id_seq.items():
    seq = seq.replace('\n', '')
    gc_count = 0
    for i in seq:
        if i == 'G' or i == 'C':
            gc_count += 1
    gc_content = (gc_count/len(seq))*100
    
    
    


        

    


    
    
# program works well, just not done, I want it to return the max gc_content



    
    



    
    



    


        
    
        
        
        
 
       



    


        
        
       
        
            
        
        

    