from itertools import permutations
import numpy as np

number = 5
order = np.arange(1, number+1, 1)
perm = list(permutations(order))

for i in perm:
    for x in range(number):
        if x < number-1 : print(str(i[x]), end=' ')
        else : print(str(i[x]))     
    

print(len(perm))
