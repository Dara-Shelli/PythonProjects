# Variables

name =  "Dara-Shelli"
empty_name = ''
not_an_empty_name = ' '
age = 12

# In python we have 3 logical operators

# 1. and
# 2. or
# 3. not

if not name:
    print("name not empty")

if not empty_name:
    print("empty name is empty")

if not not_an_empty_name.strip():
    print("not_an_empty_name is empty in value")

if age >= 18 or age < 65:
    print('Not eligible')
