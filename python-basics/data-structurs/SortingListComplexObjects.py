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

items.sort()
print(items)


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
