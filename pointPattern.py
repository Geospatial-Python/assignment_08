import random
import math
from . import point
from . import analytics
import numpy as np
import scipy.spatial as ss


class PointPattern(object):
    #initialize to list of points
    def __init__(self):
        self.points = []
        self.marks = ['lavender','orange','rose','ash','violet','magenta','cerulean']

    def add_point(self,point):
        self.points.append(point)

    def remove_point(self,index):
        del(self.points[index])

    def average_nearest_neighbor(self,mark=None):
        return analytics.average_nearest_neighbor_distance(self.points,mark)

    #find the number of coincident points
    def coin_count(self):
        count = 0
        clist = []
        for num1, point1 in enumerate(self.points):
            for num2, point2 in enumerate(self.points):
                #check that you're not comparing the same point
                if num1 != num2 and num2 not in clist: # if they are not the same point, and already counted
                    if point1 == point2:
                        count = count +1
                        clist.append(num2)
        return count


    #list all the different marks
    def mark_list(self):
        markList = []

        #go through each point and add a new mark to the mark listss
        for point in self.points:
            if point.mark not in markList:
                markList.append(point.mark)
        return markList

    #return a subset of point by mark type
    def mark_subset(self,mark):
        subset = []
        for p in self.points:
            if p.mark == mark:
                subset.append(p)
        return subset

    #where n is either provided by the user or equal to the current size of pointPattern
    def create_n_random_points(self,n =None):
        randomPoints = []
        if(n is None):
            n = len(self.points)

        for i in range(n):
            randomPoints.append(point.Point(random.randint(1,100),random.randint(1,100),random.choice(self.marks)))

        return randomPoints

    #simulate k random points patterns for Monte Carlo
    def create_k_patterns(self,k):
        return analytics.permutation_nearest_distance(self.marks,k)

    def critical_points(self):
        return analytics.critical_points(self.create_k_patterns(99))

    def compute_g(self,nsteps):
        """

        Parameters
        ----------
        nsteps: The numer of discrete d that are used to compute G(d)

        Returns
        -------

        """
        ds = np.linspace(0,1,nsteps)
        sums = 0

        for s in range(nsteps):
            oi = ds[s]
            minDist = None

            for a,b in enumerate(ds):
                temp = abs(b - oi)

                if a is not s:
                    if minDist is None: #for the first value
                        minDist = temp
                    elif minDist > temp: # if its less then the minDist, update
                        minDist = temp

            sums = sums + minDist

        g = sums/nsteps
        return g


#utilize a scipy.spatial.KDTree to compute the nearest neighbor distance

    def kDTree_nearest_neighbor(self,mark=None):
        point_array = [] # is the "tuple" that holds the arrays to be stacked
        if not mark:
            #then you dont want to look for a specific mark, and you can just find the average nearest neighbor of everything
            for p in self.points:            #add every point to the point_array
                point_array.append(p.return_array())
        else:
            #that means that there was something passed into mark and you have to only computer the nearest neighbor with that mark
            for p in self.points:
                if p.mark in mark: # passed in a possible list of marks
                    point_array.append(p.return_array())

        #now you have the vstack parameter:
        point_ndarray = np.vstack(point_array)

        #now you have the ndarray needed for kdtree, create your tree:
        kdTree = ss.KDTree(point_array)

        #now computer the nearest neighbors:
        nn_dist = []
        for p in point_ndarray:
            nearest_neighbor_distance, nearest_neighbor_point = kdTree.query(p,k=2)
            nn_dist.append(nearest_neighbor_distance[1]) #appending the second one to allow for self-neighbor

        average = np.mean(nn_dist)
        return average

    #compute the nearest neighbor distance using numpy (ndarray and mean)
    def numpy_nearest_neighbor(self,mark=None):
        shDistL = []
        point_array = []
        if not mark:
            for p in self.points:
                point_array.append(p.return_array())
        else:
            #that means a mark was passed in
            for p in self.points:
                if p.mark in mark:
                    point_array.append(p.return_array())

        #point_array = [ [1,2],[3,4],[5,6],[7.8] ]
        #using the same logic that's in analytics:
        for num1, p in enumerate(point_array):    # p = [1,2]
            shortestDistance = math.inf
            for num2, dp in enumerate(point_array):
                if num1 != num2:
                    dist = ss.distance.euclidean(p,dp)
                    if(shortestDistance > dist):
                        shortestDistance = dist
            #now add the shortest distance of that point before it moves on to a new point:
            shDistL.append(shortestDistance)
        mean_d = np.mean(shDistL) #returns the average of the array of elements, so pass in shDistL

        return mean_d

    #compute the G function using numpy
    def numpy_compute_g(self,nsteps):
        ds = np.linspace(0,1,nsteps)   #get the steps in ds
        sums =0

        for i in range(nsteps):
            oi = ds[i] #get the i'th observation
            min_dist = None

            for a,b in enumerate(ds):
                temp = np.abs(b - oi)          #changed to use numpy's implementation

                if a is not i:
                    if min_dist is None: #for the first value
                        min_dist = temp
                    elif min_dist > temp:
                        min_dist = temp
            sums = sums + min_dist
        g = sums/nsteps
        return g


    #Generate random points within some domain
    def random_points_domain(self,numPoints = 2,start=0,stop=1,seed =None):
        randomp = None
        pointsList = []
        if seed is None: #meaning no passed in starting value
            randomp = np.random
        else:
            randomp = np.random.RandomState(seed) #instantiate seed
            random.seed(seed)
        points = randomp.uniform(start,stop, (numPoints,2))    #create ndarray
        for x in range(points): #for all the points
            pointsList.append(point.Point(points[x][0],points[x][1],np.random.choice(self.marks)))
        return pointsList






