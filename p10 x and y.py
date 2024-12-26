import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

point1 = Point(3, 4)
point2 = Point(7, 1)

print("Point 1:", point1)
print("Point 2:", point2)

dist = point1.distance(point2)
print(f"Distance between {point1} and {point2} is: {dist}")
