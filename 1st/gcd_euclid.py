

import sys

def printUsage():
    print '%s  m  n' % (sys.argv[0])

def gcd_old(m, n):
    if 0 == n:
        return m
    return gcd(n, m % n)

def gcd(m, n):
    while 0 != n :
        r = m % n
        m = n
        n = r
    return m

if '__main__' == __name__:
    if 3 != len(sys.argv):
        printUsage()
        sys.exit(-1)

    d = gcd(int(sys.argv[1]), int(sys.argv[2]))
    print d

