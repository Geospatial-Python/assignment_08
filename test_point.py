'''
Created on Mar 6, 2016

@author: Max Ruiz
'''
import unittest
import random
from point import Point


#from ..point import Point

class TestPointClass(unittest.TestCase):
    def setUp(self):
        self.marks = ['burrito', 'chimichanga', 'steak', 'burger', 'chillidog',
                 'sweetpotatofries', 'beans', 'bacon', 'beijingbeef', 'friedeggs',
                 'icecream', 'brownies', 'cookie', 'bananasplit', 'almondjoy']

    def test_set_coords(self):
        _x = 5
        _y = 120
        point0 = Point(_x, _y, random.choice(self.marks))
        self.assertEqual(_x, point0.getx())
        self.assertEqual(_y, point0.gety())

    def test_check_coincident(self):
        _x = 5
        _y = 120
        point0 = Point(_x, _y, random.choice(self.marks))
        point1 = Point(5, 120, random.choice(self.marks))
        point2 = Point(_x+3, _y, random.choice(self.marks))
        point3 = Point(_x, _y+22, random.choice(self.marks))
        point4 = Point(_x+3,_y+22, random.choice(self.marks))

        self.assertTrue(point0.check_coincident(point1.getPoint()))
        self.assertFalse(point0.check_coincident(point2.getPoint()))
        self.assertFalse(point0.check_coincident(point3.getPoint()))
        self.assertFalse(point0.check_coincident(point4.getPoint()))

    def test_shift(self):
        _x = 5
        _y = 120
        point0 = Point(_x, _y, random.choice(self.marks))
        point0.shift_point(816, 80085)
        self.assertEqual((_x + 816, _y + 80085), point0.getPoint())

    def test_marked_points(self):
        random.seed(12345)

        randmarks = list()
        for x in range(20):
            randmarks.append(random.choice(self.marks))

        randmarkcnt = dict()
        for x in range(len(randmarks)):
            i = 1
            for y in range(len(randmarks)):
                if randmarks[y] == randmarks[x]:
                    i += 1
                else:
                    continue
            randmarkcnt[randmarks[x]] = i - 1

        self.assertTrue(randmarkcnt['chillidog'], 3)
        self.assertTrue(randmarkcnt['chimichanga'], 1)

    def test_class_add(self):
        point_1 = Point(11, 11)
        point_2 = Point(22, 22)
        point_3 = point_1 + point_2
        self.assertEqual(point_3.x, 33)
        self.assertEqual(point_3.y, 33)

    def test_class_eq(self):
        point_1 = Point(11,11)
        point_2 = Point(11, 11)
        self.assertFalse(point_1 == point_2)

    def test_neg(self):
        point_1 = Point(11, 22)
        point_2 = -point_1
        self.assertEqual(point_2.x, -11)
        self.assertEqual(point_2.y, -22)

