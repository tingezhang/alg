

'''
src/dst/tmp A/B/C
'''
step=1

def hanoi(n, src, dst, tmp):
    global step
    if 1 == n:
        print "step %d: move 1 from src:%s to dst:%s" % (step, src, dst)
        step = step + 1
        return

    hanoi(n-1, src, tmp, dst)
    print "step %d move %d from src:%s to dst:%s" % (step, n, src, dst)
    step = step + 1
    hanoi(n-1, tmp, dst, src)


if '__main__' == __name__:
    hanoi(5, 'A', 'C', 'B')


