def calculate_x_factor(age):
    if age <= 0:
        raise ValueError('Age cannot be 0 or less')
    return  42 / age

try:
    calculate_x_factor(-27)
except ValueError as ve:
    print(ve)