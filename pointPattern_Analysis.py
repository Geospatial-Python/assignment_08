#from . import pointPattern
#from . import point
import pysal as ps
import unittest

#utilize the example shapefile
shapefile = ps.open(ps.examples.get_path('new_haven_merged.shp'))
dbf = ps.open(ps.examples.get_path('new_haven_merged.dbf'))

for geometry, attributes in zip(shapefile,dbf):
    print(geometry,attributes)
    break

    #   so: (-72.976512, 41.337662) [' Thu, Sept. 18th 2014', 'all-cases-dead-on-arrival', ' 1605 WHALLEY AVE', ' AMITY/POND LILY', ' 01:53 p.m.']
    # I want geometry

    #First put all the points in geometry into self.points:
    pointList = []
    for geometry,attributes in zip(shapefile,dbf):
    #create a list of points to then append to a pointPattern:
        pointList.append(Point(geometry[0],geometry[1],[attributes[0],attributes[1],attributes[2],attributes[3],attributes[4]])) #third parameters is a list of marks

    #so now you have the points part of pointPattern, create an instance of pointPattern:
    point_pattern = PointPattern()
    #add points to your self.points:
    for p in pointList:
        point_pattern.add_point(p)

#how many points have a nearest neighbor closer than the distance "band" step thing
    #okay, so now you actually have the data inside pointPattern's self.points. Now you can do some analysis:

    #illustrate the use of mean nearest neighbor on the entire dataset:
    kd_avg_nn = point_pattern.kDTree_nearest_neighbor()
    print("The new_haven_merged dataset has a total average nearest neighbor distance of: ", kd_avg_nn)

    #illustrate the use of the mean nearest neighbor on a mark:
    kd_avg_nn_mark = point_pattern.kDTree_nearest_neighbor(['all-cases-dead-on-arrival'])
    print("The new_haven_merged dataset with the mark 'all-cases-dead-on-arrival' mark has a total average nearest neighbor distance of: ", kd_avg_nn_mark)

    kd_avg_nn_mark2 = point_pattern.kDTree_nearest_neighbor(['all-cases-dead-on-arrival',' 1605 WHALLEY AVE'])
    print("The new_have_merged dataset with the mark 'all-cases-dead-on-arrival' and '1605 WHALLEY AVE' marks has a total average nearest neighbor distance of", kd_avg_nn_mark2)

    #illustrate the use of the g function:
    np_compute_g = point_pattern.numpy_compute_g(12)
    print("The new_haven_merged dataset's g function results are:")
    for g in np_compute_g:
        print(g)

    np_compute_g_mark  = point_pattern.numpy_compute_g(12,['all-cases-dead-on-arrival'])
    print("The new_haven_merged dataset's g function results with a mark of 'all-cases-dead-on-arrival' are: ")
    for g in np_compute_g_mark:
        print(g)

    np_compute_g_mark2 = point_pattern.numpy_compute_g(12,['all-cases-dead-on-arrival',' 1605 WHALLEY AVE'])
    print("The new_haven_merged dataset's g function results with a marks of 'all-cases-dead-on-arrival' and ' 1605 WHALLEY AVE' are: ")
    for g in np_compute_g_mark2:
        print(g)

from point import Point
from pointPattern import PointPattern
