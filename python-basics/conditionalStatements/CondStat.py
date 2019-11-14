age = 22

if age:
    print("Will only execute if the age is evaluated as True [which it will...]"
          "meaning it holds a value other then None or default value")

if age >= 18:
    print("You're an: ")
    print("Adult")

elif age >= 13:
    print("You're a teen")

else:
    print('Child')

if age > 101:
    pass
else:
    pass

print("Program all done!")

