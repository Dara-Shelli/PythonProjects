names = ['Kenan', 'Bart', 'Patrick', 'Wouter', 'Olmo', 'Alex']

found = False

for name in names:
    if name.startswith('A'):
        print(name)
        found = True
        break

if not found:
    print("No name found starting with 'A'.")

for name in names:
    if name.startswith('X'):
        print(name)
        break
else:
    print("No name found starting with an 'X'.")
