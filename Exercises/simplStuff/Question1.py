number1 = int(input("Enter first number"))
number2 = int(input("Enter second number"))


def multi_of_sum(num1, num2):
    product = num1 * num2
    if product < 1000:
        return product
    else:
        return num1 + num2


result = multi_of_sum(number1, number2)
print("Result is", result)