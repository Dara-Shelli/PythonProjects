print("Let's start with Arithmetic operators")
first_numb = float(input("Fill in a number: "))
second_num = float(input("Fill in another number: "))
msg_result = 'result is: '

print("\nResults\n")

result = first_numb + second_num
print(f'{first_numb} {"+"} {second_num} {msg_result} {result}')

result = first_numb - second_num
print(f'{first_numb} {"-"} {second_num} {msg_result} {result}')


result = first_numb * second_num
print(f'{first_numb} {"*"} {second_num} {msg_result} {result}')

result = first_numb / second_num
print(f'{first_numb} {"/"} {second_num} {msg_result} {result}')

result = first_numb // second_num
print(f'{first_numb} {"//"} {second_num} {msg_result} {result}')

# Rest modulus:

result = first_numb % second_num
print(f'{first_numb} {"%"} {second_num} {msg_result} {result}')

# With the power of Python

result = first_numb ** second_num
print(f'{first_numb} {"**"} {second_num} {msg_result} {result}')







