global_msg = "Greeting Globally"


def greet():
    global_msg = "Change is good"

    if True:
        message_local = "Greeting local"

    print(message_local)


greet()
print(global_msg)


evil_global_variable = "You were warned!"


def evil_function():
    global evil_global_variable
    evil_global_variable = "You should have listed!"


evil_function()
print(evil_global_variable)
