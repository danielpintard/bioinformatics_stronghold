#bottom up, no recursion
def fib(n):
    if n == 1  or n == 2 : return 1
    seq = [None] * (n + 1)
    seq[1] = 1
    seq[2] = 1
    for idx in range(3, n + 1):
        seq[idx] = seq[idx - 1] + seq[idx - 2]
    return seq[n] 

print(fib(100))  