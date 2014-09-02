
import math



def prime_sieve(n):
    N = range(1, n + 1)
    M = range(2, int(math.floor(math.sqrt(n))) + 1)
    for p in M:
        if 0 != N[p - 1] :
            j = p * p
            while j <= n :
                N[j - 1] = 0
                j = j + p

    R = []
    for i in range(n):
        if 0 != N[i] and 1 != N[i]:
            R.append(N[i])
    return R


if '__main__' == __name__:
    L = prime_seive(1000000)
    print L

