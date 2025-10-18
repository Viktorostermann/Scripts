from math import sqrt

def points_distance(x1, y1, x2, y2):
    dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(dist)

points_distance(1, 2, 3, 5)