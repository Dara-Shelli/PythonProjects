items = [
    ('Product1', 10),
    ('Product2', 420),
    ('Product3', 30),
    ('Product4', 5),
    ('Product5', 55),
    ('Product6', 77),
    ('Product7', 1110),
    ('Product8', 31)

]


items.sort(key=lambda item: item[1])
print(items)