data = open('/Users/danielpintard/Downloads/rosalind_iev.txt', 'r') 
# data = open('ex_off_samdata.txt') 

num_couples = [int(i) for i in data.readline().strip().split()]

for i in range(len(num_couples)):
    probabilities = [1, 1, 1, 0.75, 0.5, 0]
    offspring = 2
    equation = sum(num_couples[i] * probabilities[i] * offspring for i in range(len(probabilities))) 
    print(equation)

