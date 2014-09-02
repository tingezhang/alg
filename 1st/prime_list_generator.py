
import random
from prime_sieve import prime_sieve

def prime_list_generator(max_integer, list_len):
    P = prime_sieve(max_integer)
    P_len = len(P)

    L = []
    for i in range(list_len):
        L.append(P[int(random.random() * P_len)])

    return L

if '__main__' == __name__:
    L = prime_list_generator(100, 5)
    print L
