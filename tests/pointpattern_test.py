import unittest

from ..pointpattern import PointPattern
from .. import point

class TestPointPattern(unittest.TestCase):
    def setUp(self):
        self.test = PointPattern()
        self.test.add_point(point.Point(2, 5, mark='North'))
        self.test.add_point(point.Point(4, 1, mark='North'))
        self.test.add_point(point.Point(2, 5, mark='South'))
        self.test.add_point(point.Point(1, 1))

    def test_coincident(self):
        self.assertEqual(self.test.count_coincident_points(), 2)

    def test_list_marks(self):
        self.assertEqual(self.test.list_marks(), ['North', 'South'])

    def test_return_subset(self):
        self.assertEqual(len(self.test.return_subset('North')), 2)

    def test_generate_points(self):
        self.assertEqual(len(self.test.create_random_points(20)), 20)

    def test_realizations(self):
        self.assertEqual(len(self.test.create_realizations(20)), 20)

    def test_g_function(self):
        self.assertAlmostEqual(self.test.compute_g(100), 1.0101, places=4)

    def test_kdtree_nearest(self):
        self.assertAlmostEqual(self.test.average_nearest_neighbor_distance_kdtree(), 0.75, places=4)