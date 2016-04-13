import utils


def find_largest_city(gj):

    city = None
    max_population = 0
    for item in gj["features"]:
        props = item["properties"]
        if props["pop_max"] > max_population:
            max_population = props["pop_max"]
            city = props["adm1name"]

    return city, max_population


def average_nearest_neighbor_distance(points_list, mark = None):
   
    points = None
    if mark is None:
        
        points = points_list
    else:
        points = list(filter(lambda current_point: current_point.mark['color'] == mark, points_list))

    mean_d = 0
    temp_nearest_neighbor = None
    
    for i, point in enumerate(points):
        for j, otherPoint in enumerate(points):
            if i == j:
                continue
            current_distance = utils.euclidean_distance((point.x, point.y), (otherPoint.x, otherPoint.y))
            if temp_nearest_neighbor is None:
                temp_nearest_neighbor = current_distance
            elif temp_nearest_neighbor > current_distance:
                temp_nearest_neighbor = current_distance
        mean_d += temp_nearest_neighbor
        temp_nearest_neighbor = None
    mean_d /= len(points)

    return mean_d


def permutations(p=99, mark=None):
    n = 100
    to_return = []
    for i in range(p):
        to_return.append(
            average_nearest_neighbor_distance(
                utils.create_random(n),
                mark
            )
        )
    return to_return


def compute_critical(p):
    return min(p), max(p)
