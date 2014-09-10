'''
Design an algorithm for the following problem: Given a set ofnpoints in the
Cartesian plane, determine whether all of them lie on the same circumference.
'''

'''
1. the line pass through point A(x1, y1), B(x2, y2)
(y - y1) = ((y2 - y1)/(x2 - x1))(x - x1)
'''

'''
2. the midnormal Lm of two point A(x1, y1) and B(x2, y2)
2.1 slope of Lab is (y2 - y1)/(x2 - x1)
2.2 slope of Lm is -(x2 - x1)/(y2 - y1)
2.3 mid point of A, B  ((x1 + x2)/2, (y1 + y2)/2)
2.4 L:  y - (y1 + y2)/2 = (-(x2 - x1)/(y2 - y1)) * (x - (x1 + x2)/2)
    => y + (x2 - x1)x/(y2 - y1) = (y1 + y2)/2 + (x1 + x2)(x2 - x1)/(y2 - y1)
'''

'''
3 cross point of L1 and L2
3.1 L1  ax + by = c
3.2 L1  mx + ny = p
3.3 matrix operation


3.1 L1 y = ax + b
3.2 L2 y = mx + n
       (a -m)x = n -b => x = (n - b)/(a - m)
http://blog.csdn.net/xuy1202/article/details/6924746
'''

import random

def generatePointList(size, max_value):
    ret_list = []

    while size > 0:
        x = int((random.random() - 0.5) * max_value)
        y = int((random.random() - 0.5) * max_value)
        ret_list.append((x, y))
        size = size - 1

    return ret_list

def calculateCrossPoint(a, b, m, n):
    x = (n - b)/(a - m)
    y = a * x + b
    return (x, y)

def calculateSlope(x1, y1, x2, y2):
    return (y2 - y1)/(x2 - x1)

'''
2.4 L:  y - (y1 + y2)/2 = (-(x2 - x1)/(y2 - y1)) * (x - (x1 + x2)/2)
    => y + (x2 - x1)x/(y2 - y1) = (y1 + y2)/2 + (x1 + x2)(x2 - x1)/(y2 - y1)
'''
def calculateMidnormal(x1, y1, x2, y2):
    xm = (x1 + x2)/2
    ym = (y1 + y2)/2

    k = (x1 - x2)/(y2 - y1)
    b = (y1 + y2)/2 + (x1 + x2) * (x2 - x1)/(y2 - y1)
    return (k, b)

def calculate4PointCenterOfCircle(point1, point2, point3, point4):
    L1 = calculateMidnormal(point1[0], point1[1], point2[0], point2[1])
    L2 = calculateMidnormal(point3[0], point3[1], point4[0], point4[1])

    point = calculateCrossPoint(L1[0], L1[1], L2[0], L2[1])
    return point

def calculateCenterOfCircle(point_list):
    size = len(point_list)

    point1 = calculate4PointCenterOfCircle(point_list[0], point_list[1], point_list[1], point_list[2])
    print point1

    for i in range(2, size - 1):
        point = calculate4PointCenterOfCircle(point_list[0], point_list[1], point_list[i], point_list[i + 1])
        print point
        if abs(point[0] - point1[0]) + abs(point[1] - point1[1]) > 0.0001:
            print "fail"
            return False

    print "success"
    return True



def main():
    point_list = generatePointList(10, 1000)
    calculateCenterOfCircle(point_list)




if '__main__' == __name__:
    main()
