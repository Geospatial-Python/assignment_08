from point import PointPattern
import pysal as ps

# Open the shapefile using the example above and read in the points
# attributes[1], in the above example, is the mark
shapefile = ps.open(ps.examples.get_path('new_haven_merged.shp'))
dbf = ps.open(ps.examples.get_path('new_haven_merged.dbf'))

pList = []

for geometry, attributes in zip(shapefile, dbf):
    pList.append(Point(geometry[0],geometry[1],attributes[1]))
    

pattern = PointPattern(pList)


# Run a few tests to explore the dataset.
nn = PointPattern.nearest_neighbot_KD(pattern)
print('This interesting mark has a nearest neighbor distance of {}'.format(nn))


# Use your monte carlo simulation code to see if the result is statistically significant
smallest, largest = pattern.critical_points(pattern.utils.permutations())
if check_significant(smallest, largest):
    print('The mark is significant.')
else:
    print('The mark is not significant.')
