import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import keyboard


# defining the point(x,y)
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


# defining the node
class Node():
    def __init__(self, x0, y0, w, h, points):
        self.x0 = x0
        self.y0 = y0
        self.width = w
        self.height = h
        self.points = points
        self.children = []

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_points(self):
        return self.points


# defining my Quad
class QTree():
    def __init__(self, k, points):
        # defining threshold for the points
        self.threshold = k
        # defining n random points inside the range
        self.points = points
        # defining the root node
        self.root = Node(0, 0, 10, 10, self.points)

    def add_point(x, y):
        self.points.append(Point(x, y))

    def get_points(self):
        return self.points

    def subdivide(self):
        recursive_subdivide(self.root, self.threshold)

    # drawing the reactangle and points
    def graph(self):
        fig = plt.figure(figsize=(12, 8))
        plt.title("My QTree")
        ax = fig.add_subplot(111)
        c = find_children(self.root)

        areas = set()
        for el in c:
            areas.add(el.width * el.height)

        for n in c:
            ax.add_patch(patches.Rectangle((n.x0, n.y0), n.width, n.height, fill=False))
        x = [point.x for point in self.points]
        y = [point.y for point in self.points]
        plt.plot(x, y, 'go')
        plt.show()
        return


def recursive_subdivide(node, k):
    # checking if im ok with the threshold
    if len(node.points) <= k:
        return

    w_ = float(node.width / 2)
    h_ = float(node.height / 2)

    # splitting into the 4 children
    p = contains(node.x0, node.y0, w_, h_, node.points)
    x1 = Node(node.x0, node.y0, w_, h_, p)
    recursive_subdivide(x1, k)

    p = contains(node.x0, node.y0 + h_, w_, h_, node.points)
    x2 = Node(node.x0, node.y0 + h_, w_, h_, p)
    recursive_subdivide(x2, k)

    p = contains(node.x0 + w_, node.y0, w_, h_, node.points)
    x3 = Node(node.x0 + w_, node.y0, w_, h_, p)
    recursive_subdivide(x3, k)

    p = contains(node.x0 + w_, node.y0 + h_, w_, h_, node.points)
    x4 = Node(node.x0 + w_, node.y0 + h_, w_, h_, p)
    recursive_subdivide(x4, k)

    node.children = [x1, x2, x3, x4]


# checking if a point exists in a node
def contains(x, y, w, h, points):
    pts = []
    for point in points:
        if point.x >= x and point.x < x + w and point.y >= y and point.y < y + h:
            pts.append(point)
    return pts


# recursively finding the children
def find_children(node):
    if not node.children:
        return [node]
    else:
        children = []
        for child in node.children:
            children += (find_children(child))
    return children


def test(k, points):
    # arithmos shmeiwn

    qt = QTree(k, points)

    qt.subdivide()
    qt.graph()


def main():
    n = 200
    k = 1
    #points1 = [[1, 1], [5, 5], [8, 8], [8, 2]]
    points = [Point(random.uniform(0, 10), random.uniform(0, 10)) for x in range(n)]
    #points = [Point(x[0], x[1]) for x in points1]
    test(k, points)


if __name__ == "__main__":
    main()
