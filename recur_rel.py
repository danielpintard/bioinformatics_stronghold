def rabbit_fib(n, k):
    if n == 1  or n == 2 : return 1
    seq = [None] * (n + 1)
    seq[1] = 1 
    seq[2] = 1 
    for i in range(3, n + 1):
        seq[i] = seq[i - 1] + (seq[i - 2] * k)
    print(seq[1:7])
    return seq[n] 

print(rabbit_fib(35,2)) 