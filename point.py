from utils import *
import numpy as np
import scipy.spatial as ss
from nose.tools import set_trace

class Point(object):
  def __init__(self, x, y, mark={}):
    self.x = x
    self.y = y
    self.mark = mark

  def __add__(self, other):
    return self.x + other.x, self.y, other.y

  def __div__(self, other):
    return self.x / other.x, self.y, other.y

  def __sub__(self, other):
    return self.x - other.x, self.y, other.y

  def create_random_marked_points(self, n, marks=[]):
    list_o_random_points = []
    for i in range(n):
      random_point = Point(random.seed, random.seed, random.choice(marks))
      list_o_random_points.append(random_point)
    return list_o_random_points

  def check_coincident(self, other):
    return check_coincident((self.x, self.y), (other.x, other.y))

  def shift_point(self, x_shift, y_shift):
    return shift_point((self.x, self.y), x_shift, y_shift)

class PointPattern:
  def __init__(self):
    self.points = []

  def average_nearest_neighbor_distance(self, mark=None):
    return utils.average_nearest_neighbor_distance(self.points, mark)

  def list_of_marks(self):
    list_o_marks = []
    for point in self.points:
      if point.mark not in list_o_marks:
        list_o_marks.append(point.mark)
    return list_o_marks

  def coincident_points(self):
    number_of_coincidents = 0
    list_o_coincidents = []
    for point in range(len(self.points)):
      for neighbor in range(len(self.points)):
        if point in list_o_coincidents or point==neighbor:
          continue
        # This was easier to make work than check_coincident
        if self.points[point] == self.points[neighbor]:
          number_of_coincidents = count + 1
          list_o_coincidents.append(neighbor)
    return number_of_coincidents

  def subset_of_points_by_mark_type(self, mark):
    subset_list = []
    for point in self.points:
      if point.mark == mark:
        subset.append(point)
    return subset_list

  def generate_n_random_points(self, n=None):
    n_random_points = []
    if n is None: 
      n = len(self.points)

    for i in range(n):
      n_random_points.append(Point(random.random(), random.random()))
    return n_random_points


  def generate_k_patterns(self, k):
    return analytics.permutations(self.marks, k)

  def nearest_neighbor_critical_points(self):
    return analytics.compute_critical(self.generate_k_patterns(100))

  def nearest_neighbor_KD(self):
    list_o_points = []
    distances = []

    points = self.points
    for point in points:
      list_o_points.append(point.array())
    temp = np.vstack(list_o_points)

    dist_KD = ss.KDTree(temp)
    
    for point in temp:
      nearest_neighbor_distance, nearest_neighbor = kdtree.query(p, k=2)
      distances.append(nearest_neighbor_distance[1])

    return np.array(distances)

  def compute_g(self, nsteps):
    ds = np.linspace(0, 100, nsteps)
    sum_g = 0

    for n in range(nsteps):
      oi = ds[n]
      min_d = None
      for i, j in enumerate(ds):
        temp = abs(j - oi)
        if i is n:
          continue
        if min_d is None:
          min_d = temp
        elif min_d > temp:
          min_d = temp
        else:
          continue
      sum_g = sum_g + min_d
    return sum_g / nsteps