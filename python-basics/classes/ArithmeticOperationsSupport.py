class Human:

    def __init__(self, surname, name, intelligence):
        self.surname = surname
        self.name = name
        self.intelligence = intelligence

    def __str__(self):
        return f'{self.surname} {self.name}'

    def __add__(self, other):
        if isinstance(other, Human):
            return self.intelligence + other.intelligence


darashelli = Human('Tvisher', 'Dara', 8000)
snoop = Human('Snoop', 'Leon', 420)

print(f'Combined intell: {darashelli + 1}')


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'Point: x: {self.x}, y: {self.y} '


first_point = Point(14, 45)
sec_point = Point(84, 3)

combined_point = first_point + sec_point
print(combined_point)