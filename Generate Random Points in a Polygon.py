import numpy as np
from shaply.geometry import Point

def Random_points_in_polygon(polygon, number):
    points = []
    minx, miny, maxx, maxy = polygon.bounds
    while len(points) < number:
        pnt = point(np.random.uniform(minx, maxx), np.random.uniform (miny, maxy))
        if polygon.contains(pnt):
            points.append(pnt)
            return points
        polygon = Polygon([[0, 0], [0, 2], [1.5, 1], [0.5, -0.5], [0, 0]])
        points = Random_Points_in_Polygon(polygon, 100)

        # Plot the polygon
        xp, yp = polygon.exterior.xy
        plt.plot(xp, yp)

        # Plot the list of points
        xs = [point.x for point in points]
        ys = [point.y for point in points]
        plt.scatter(xs, ys, color="red")
        plt.show()