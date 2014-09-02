

from prime_sieve import prime_sieve

def prime_factorization(n):
    P = prime_sieve(n)

    F = []
    for p in P:
        while 0 == (n % p):
            F.append(p)
            n = n / p
        if 1 == n:
            break

    return F


if '__main__' == __name__:
    F = prime_factorization(65534)
    print F
