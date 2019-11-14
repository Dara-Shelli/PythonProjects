numbers = [1, 2]

#print([3])

try:
    age = int(input('Please fill in your age: '))
except ValueError:
    print("You did not enter a valid age")
else:
    print('Executed if and only in no error was thrown.')

print('Execution continues?')