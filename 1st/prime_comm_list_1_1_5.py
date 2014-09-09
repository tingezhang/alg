
'''
Design an algorithm to find all the common elements in two sorted lists of
numbers. For example, for the lists 2, 5, 5, 5 and 2, 2, 3, 5, 5, 7, the output
should be 2, 5, 5. What is the maximum number of comparisons your algorithm
makes if the lengths of the two given lists aremandn,respectively?
'''

from prime_list_generator import prime_list_generator
from gcd_euclid import gcd as euclid_gcd
import sys


def prime_calc_comm_list(prime_list_a, prime_list_b):
    comm_list = []
    prime_a = 1
    prime_b = 1
    for prime_num in prime_list_a:
        prime_a = prime_num * prime_a
    for prime_num in prime_list_b:
        prime_b = prime_num * prime_b

    gcd_value = euclid_gcd(prime_a, prime_b)
    if len(prime_list_a) < len(prime_list_b):
        prime_list = prime_list_a
    else:
        prime_list = prime_list_b

    for prime_num in prime_list:
        while 0 == (gcd_value % prime_num):
            comm_list.append(prime_num)
            gcd_value = gcd_value / prime_num
        if 1 == gcd_value:
            break

    return comm_list

def printUsage():
    print 'usage: %s LIST_A_LEN LIST_B_LEN' % sys.argv[0]
    sys.exit(-1)

def main():
    if 3 != len(sys.argv):
        printUsage()

    list_a_len = int(sys.argv[1])
    list_b_len = int(sys.argv[2])

    prime_list_a = prime_list_generator(1000, list_a_len)
    prime_list_b = prime_list_generator(1000, list_b_len)
    comm_list = prime_calc_comm_list(prime_list_a, prime_list_b)

    print prime_list_a
    print prime_list_b
    print comm_list


if '__main__' == __name__:
    main()


