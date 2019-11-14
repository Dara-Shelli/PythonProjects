class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def draw(self):
        print(f'Point ({self.x}, {self.y}, {self.z})')


point = Point(420, 18, 27)

point.x = 111
point.y = 222
point.z = 333

print('x coordinate:', point.x)
print('y coordinate:', point.y)
print('z coordinate:', point.z)

point.draw()
