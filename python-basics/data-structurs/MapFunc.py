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

#prices = []
#for item in items:
#   prices.append(item[1])

map_only_prices = list(map(lambda single_item: single_item[1], items))

print(map_only_prices)
