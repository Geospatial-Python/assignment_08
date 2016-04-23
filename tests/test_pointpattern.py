import unittest
from .. import point
from nose.tools import set_trace

class TestPointPattern(unittest.TestCase):
	def setUp(self):
		pass

	def test_kd_comparison(self):
		points = point.PointPattern.generate_n_random_points(self, 100)
		# ~~!@~!@~!@~!@~@~!@~!@!~~
		# This is brutal! Having trouble calling class methods on objects when running tests
		# because it keeps checking TestPointPattern instead of PointPattern when inside the actual class functions (in point.py)
		# I just want to add points to an instance of PointPattern, but in point.py, self keeps referring to this test class.
		# ~~!@~!@~!@~!@~@~!@~!@!~~
		# kd_comparison = points.nearest_neighbor_KD()
		# set_trace()
