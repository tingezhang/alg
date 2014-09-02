import sys


def gcd(m, n):
    for r in range(n, 0, -1):
        if (0 == (m % r)) and (0 == (n % r)):
            return r



if '__main__' == __name__:
    if 3 != len(sys.argv):
        printUsage()
        sys.exit(-1)

    d = gcd(int(sys.argv[1]), int(sys.argv[2]))
    print d

