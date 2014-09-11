
import sys

pattern_stringa = [0] * 52
pattern_stringb = [0] * 52


def print_usage():
    print "%s  stringa stringb" % sys.argv[0]
    sys.exit(-1)

def calculate_idx(ch):
    if ord(ch) >= ord('a')  and ord(ch) <= ord('z'):
        return ord(ch) - ord('a')
    elif ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
        return ord(ch) - ord('A') + 26
    else:
        return -1

def anagram_checking():
    if 3 != len(sys.argv) :
        print_usage()


    if len(sys.argv[1]) != len(sys.argv[2]) :
        print "anagram checking fail, len is not the same"
        sys.exit(-4)

    for a in sys.argv[1]:
        idx = calculate_idx(a)
        if idx < 0:
            print "invalid string %s" % sys.argv[1]
            sys.exit(-2)
        pattern_stringa[idx] = pattern_stringa[idx] + 1

    for b in sys.argv[2]:
        idx = calculate_idx(b)
        if idx < 0:
            print "invalid string %s" % sys.argv[2]
            sys.exit(-3)
        pattern_stringb[idx] = pattern_stringb[idx] + 1

    for idx in range(52):
        if pattern_stringb[idx] != pattern_stringa[idx]:
            print "anagram checking fail"
            sys.exit(-4)
    print "anagram checking success"
    sys.exit(0)



if '__main__' == __name__:
    anagram_checking()
