def mortal_rabbits(n, m):
# n = genertions
# m = survival time
    if n == 1 or n == 2: return 1
    seq = [None] * (n+1) 
    seq[1] = 1
    seq[2] = 1 
    for i in range(3, n + 1):
        # reproduction as normal
        if i <= m:
            seq[i] = seq[i - 1] + seq[i - 2]
        elif i == m + 1:
            seq[i] = seq[i - 1] + seq[i - 2] - 1 
        else:
            seq[i] = seq[i - 1] + seq[i - 2] - seq[i - (m + 1)]
    print(seq[1:7])
    return seq[n] 

print(mortal_rabbits(6, 3))