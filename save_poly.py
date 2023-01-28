from shapely.geometry import Polygon, Point
from svg_turtle import SvgTurtle
import numpy as np


def draw_poly1(polygon, number):
    points1 = []
    minx, miny, max1, maxy = polygon.bounds
    while len(points1) < number:
        pnt = Point(np.random.uniform(minx, max1), np.random.uniform(miny, maxy))
        if polygon.contains(pnt):
            points1.append(pnt)
    return points1


poly1 = Polygon(([[0, 0], [0, 2], [1.5, 1], [0.5, -0.5], [0, 0]]))
points = draw_poly1(poly1, 100)


def writefile(draw_poly1, file, w, h):
    tx = SvgTurtle(w, h)
    draw_poly1(tx)
    tx.save_as(file)


def main():
    writefile(draw_poly1, 'Poly.svg', 500, 500)
    print("File Created")
