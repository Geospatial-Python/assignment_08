import json
def read_geojson(input_file):

    with open(input_file, 'r') as fp:
        gj = json.load(fp)
    return gj
