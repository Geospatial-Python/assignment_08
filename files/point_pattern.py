from .point import Point
from . import analytics
import random
import numpy as np
import scipy.spatial as ss


class PointPattern(object):
    def __init__(self):
        self.points = []

    def add_point(self, point):
        self.points.append(point)
        
    def remove_point(self, index)
      try:
         del(self.points[index])
      except:
         pass

    def average_nearest_neighbor_distance(self, mark=None):
    
        return analytics.average_nearest_neighbor_distance(self.points, mark)
    
    def average_nearest_neighbor_distance_kdtree(self)
    nn_distances = []
    for p in points:
    nearest_neighbor_distance, nearest_neighbor = kdtree.query(p, k=2)
    nn_distances.append(nearest_neighbor_distance[0])
    nn_distances.append(nearest_neighbor_distance[1])
    nn_distances = np.array(nn_distances)
    
    print(nearest_neighbor_distance, nearest_neighbor)
        
    def average_nearest_neighbor_distance_numpy(self)
        points_list = []
        for point in self.points:
            point_list.append(point.array())
        ndarray = np.array(point_list)
        nn = []
        temp_nn = None
        
       
    def number_of_coincident(self):
      
      nc = 0
      indexed = []
      
      for i in range(len(self.points)):
            for j in range(len(self.points)):
               if j in indexed:
                   continue
               if i == j:
                  continue
               if self.points[i] == self.points[j]:
                  nc += 1
                  indexed.append(j)
        return nc
    
    def list_marks(self):
      
      marks = []
       for point in self.points:
           if point.mark is not None and point.mark not in marks:
               marks.append(point.mark)
       return marks
       
    def find_subset_with_mark(self, mark):
    
        marked_points = []
        for points in self.points:
            if points.mark == mark:
               marked_points.append(points)
        return marked_points
    
    def generate_random_points(self, n=None):
    
        if n is None:
           n = len(self.points)
        random_points = []
        self.marks = ['Blue', 'Rare', 'Medium-Rare', 'Medium', 'Medium-Well', 'Well-Done']

        for i in range(n):
           random_points.append(Point(round(random.random(), 2), round(random.random(), 2), random.choice(self.marks)))
        return random_points
        
    def generate_realizations(self, k):
    
        return analytics.permutations(k)
    
    def get_critical_points(self):
    
       return analytics.compute_critical(self.generate_realizations(100))
       
    def compute_g(self, nsteps):
    
       disc_step = np.linspace(0, 1, nsteps)
       sum = 0
       for i in range(nsteps):
           i_step = disc_step[i]
           min_dist = None
           for j in range(len(disc_step)):
                if i == j:
                    continue
                if min_dist = None:
                    min_dist = abs(disc_step[j] - i_step)
                else:
                    if abs(disc_step[j] - i_step) < min_dist:
                        min_dist = abs(disc_step[j] - i_step)
                    else:
                        min_dist = min_dist
            sum += min_dist

       return sum / nsteps
