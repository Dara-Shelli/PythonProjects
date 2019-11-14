letters = ["a", "b", "c", "d"]

print(f'first item: {letters[0]}')
print(f'first item: {letters[-1]}')

#letters[0] = letters[0].upper()

print(f'original list id: {id(letters)}')
print(f'copied list id: {id(letters[:])}, {letters[:]}')
