numbers = list(range(5))

first = numbers[0]
second = numbers[1]
last = [-1]

first, sec, third, fourth, fifth = numbers
first, sec, third = numbers[0:3]

print(first, sec, third)

bigger_list = list(range(1001))

first, second, *others = bigger_list[::-1]
print(f'first:{first}')
print(f'second:{second}')
print(f'others:{others}')
