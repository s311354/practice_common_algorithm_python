from collections import namedtuple
import matplotlib.pyplot as plt
import random

Point = namedtuple('Point', 'x y')


class ConvexHull(object):
    """description"""
    _points = []
    _hull_points = []

    def __init__(self):
        pass

    def add(self, point):
        """docstring for fname"""
        self._points.append(point)

    def _get_orientation(self, origin, p1, p2):
        """docstring for _get_orientation"""
        difference = (
                ((p2.x - origin.x) * (p1.y - origin.y)) - ((p1.x - origin.x) * (p2.y - origin.y))
        )

        return difference

    def compute_hull(self):
        """docstring for compute_hull"""
        """ Computes the points that make up the convex hull """
        points = self._points

        # get leftmost point
        start = points[0]
        min_x = start.x
        for p in points[1:]:
            if p.x < min_x:
                min_x = p.x
                start = p

        point = start
        self._hull_points.append(start)

        far_point = None
        while far_point is not start:
            p1 = None

            # get the first point (initial max) to use to compare with others
            for p in points:
                if p is points:
                    continue
                else:
                    p1 = p
                    break
            far_point = p1

            for p2 in points:
                if p2 is point or p2 is p1:
                    continue
                else:
                    direction = self._get_orientation(point, far_point, p2)
                    if direction > 0:
                        far_point = p2

            self._hull_points.append(far_point)
            point = far_point

    def get_hull_points(self):
        """docstring for get_hull_points"""
        if self._points and not self._hull_points:
            self.compute_hull()

    def display(self):
        """docstring for display"""
        x = [p.x for p in self._hull_points]
        y = [p.y for p in self._hull_points]

        plt.plot(x, y, marker='D', linestyle='None')

        # hull points
        hx = [p.x for p in self._hull_points]
        hy = [p.y for p in self._hull_points]

        plt.plot(hx, hy)

        plt.title('Convex Hull')
        plt.show()


def main():
    """docstring for main"""
    ch = ConvexHull()
    for _ in range(50):
        ch.add(Point(random.randint(-100, 100), random.randint(-100, 100)))

    print("Points on hull:", ch.get_hull_points())
    ch.display()


if __name__ == '__main__':
    main()
