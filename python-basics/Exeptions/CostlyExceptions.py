from timeit import timeit

code1 = """
def calculate_x_factor(age):
    if age <= 0:
        raise ValueError('Age cannot be 0 or less')
    return  42 / age

try:
    calculate_x_factor(-27)
except ValueError as ve:
    pass
"""

code2 = """
def calculate_x_factor(age):
    if age <= 0:
        return None
    return  42 / age
    
  
x_factor =  calculate_x_factor(-27)
if x_factor == None:
    pass
"""

msg = 'Execution time of our code: '

print(f'{msg} code1 | {timeit(code1, number=10_000)}')
print(f'{msg} code1 | {timeit(code2, number=10_000)}')




