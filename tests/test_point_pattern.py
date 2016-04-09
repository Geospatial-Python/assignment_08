from .. import point_pattern


import unittest

class TestPointClass(unittest.TestCase):

    def setUp(self):

        new_point_list=[point_pattern.Point(1,1,'red'),point_pattern.Point(2,2,'red'),point_pattern.Point(1,1,'blue')]
        self.point_pattern = point_pattern.PointPattern(new_point_list)
        

    def test_nearest_neighbor(self):

        self.assertAlmostEqual(self.point_pattern.average_nearest_neighbor_distance_KDTree(),self.point_pattern.average_nearest_neighbor_distance())
        self.assertAlmostEqual(self.point_pattern.average_nearest_neighbor_distance_np(),self.point_pattern.average_nearest_neighbor_distance())
        self.assertAlmostEqual(self.point_pattern.average_nearest_neighbor_distance(), 0.471, places=3)

    def test_number_of_coincident_points(self):

        self.assertEqual(self.point_pattern.number_of_coincident_points(),2)

    def test_list_subset_of_points(self):

         self.assertEqual(len(self.point_pattern.list_subset_of_points("red")),2)

    def test_list_marks(self):

        self.assertEqual(self.point_pattern.list_marks(), ['blue', 'red'])

    def test_create_random(self):

        self.assertEqual(len(self.point_pattern.create_random_marked_points(marks= ['red', 'blue'])), 3)

    def test_generate_realizations(self):

        self.assertEqual(len(self.point_pattern.create_realizations(23)), 23)

    def test_compute_g(self):

        self.assertAlmostEqual(self.point_pattern.compute_g(10), 0.111,places=3)
        self.assertAlmostEqual(self.point_pattern.compute_g(100), 0.010,places=3)
        self.assertAlmostEqual(self.point_pattern.compute_g(1000), 0.001,places=3)

