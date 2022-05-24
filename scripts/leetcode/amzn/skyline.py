"""

Skyline

Given all buildings in a city return skyline

"""


def get_skyline(rectangles):
    points = []
    for r in rectangles:
        points.append([r[0], r[2]])
        points.append([r[1], 0])
        for p in points:
            if r[0] <= p[0] and p[0] < r[1]:
                p[1] = max(p[1], r[2])
    return points


print(get_skyline([[1, 2, 10], [4, 6, 5], [0.5, 10, 20]]))
