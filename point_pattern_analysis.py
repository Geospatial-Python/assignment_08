from point_pattern import PointPattern
import pysal as ps

shapefile = ps.open(ps.examples.get_path('new_haven_merged.shp'))
dbf = ps.open(ps.examples.get_path('new_haven_merged.dbf'))

for geometry, attributes in zip(shapefile, dbf):

    break
