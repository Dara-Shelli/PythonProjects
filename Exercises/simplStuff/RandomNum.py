from random import randint

name = input("Please enter your name: ")
print("Welcome to the Game, " + name)


def game():
    rand_num = randint(0, 100)
    print("\n Select number 1 and 100")
    print("just 6 chances to guess number")

    i = 1
    r = 1
    while i < 7:
        user_number = int(input("Enter your number: "))
        if user_number < rand_num:
            print("\n" + name + ", The number is greater")
            print("you have " + str(6 - i) + " chances left")
            i = i + 1
        elif user_number > rand_num:
            print("\n" + name + ", The number is smaller")
            print("you have " + str(6 - i) + " chances left")
        elif user_number == rand_num:
            print("You guessed right")
            r = 0
            break
        else:
            print("This is an invalid number. Try again.")
            continue
    if r == 1:
        print("The game is lost!")
        print("The number was = " + str(rand_num))


game()




