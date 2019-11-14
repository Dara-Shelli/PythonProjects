class Point:

    default_col = 'red'

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def zero(cls):
        return cls(0, 0, 0)

    def draw(self):
        print(f'x: {self.x}, y: {self.y}, z: {self.z}')


point = Point.zero()
second_point = point.zero()
second_point.draw()