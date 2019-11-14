from random import randint

guess = 0
answer = randint(0, 100)


while answer != guess:
    guess = int(input('make a guess[0 -100]'))
    if answer < guess:
        print("Lower!")
    elif answer > guess:
        print("higher!")
    else:
        print("Guessed right")