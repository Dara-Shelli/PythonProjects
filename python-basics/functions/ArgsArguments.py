def multiply(a, b):
    return a * b


print(multiply(2, 5))


def multiply_list_1(*list_values):
    print(type(list_values), list_values)


multiply_list_1(1)
multiply_list_1(1)
multiply_list_1(1, 5, 4, 5)


