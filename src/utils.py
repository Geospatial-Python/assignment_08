import math
import random

from . import point


def create_random(n):
    rng = random.Random()
    marks = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    to_return = []
    for i in range(n):
        to_return.append(point.Point(
            round(rng.uniform(0, 1), 2),
            round(rng.uniform(0, 1), 2),
            color=rng.choice(marks)))
    return to_return


def check_significant(lower, upper, distance):
    return (distance < lower) or (distance > upper)


def mean_center(points):
    x = 0
    y = 0
    n = 0
    for point in points:
        x += point[0]
        y += point[1]
        n += 1

    x /= n
    y /= n

    return x, y


def minimum_bounding_rectangle(points):
    mbr = [None,None,None,None]
    for point in points:

        if mbr[0] is None:
            mbr[0] = point[0]
            mbr[1] = point[1]
            mbr[2] = point[0]
            mbr[3] = point[1]
        else:

            if point[0] < mbr[0]:
                mbr[0] = point[0]
            if point[1] < mbr[1]:
                mbr[1] = point[1]
            if point[0] > mbr[2]:
                mbr[2] = point[0]
            if point[1] > mbr[3]:
                mbr[3] = point[1]

    return mbr


def mbr_area(mbr):
    area = (mbr[3] - mbr[1]) * (mbr[2] - mbr[0])
    return area


def expected_distance(area, n):
    expected = 0.5 * ((area / n) ** 0.5)
    return expected


def manhattan_distance(a, b):
    distance =  abs(a[0] - b[0]) + abs(a[1] - b[1])
    return distance


def euclidean_distance(a, b):
    distance = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    return distance


def shift_point(point, x_shift, y_shift):
    x = getx(point)
    y = gety(point)
    x += x_shift
    y += y_shift
    return x, y


def check_coincident(a, b):
    return a == b


def check_in(point, point_list):
    return point in point_list


def getx(point):
    return point[0]


def gety(point):
    return point[1]
