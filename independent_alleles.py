from scipy.special import binom

def second_law(k, N):
    def p(n, k):
        return binom(2**k, n) * 0.25**n * 0.75**(2**k-n)
    return 1 - sum(p(n, k) for n in range(N))

print(round(second_law(7,20)))

