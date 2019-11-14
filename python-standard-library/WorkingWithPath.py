#home/dara-shelli/Desktop/password.txt


from pathlib import Path

new_line = "\n"

unix_path_1 = Path('/home/dara-shelli/Desktop/password.txt')
unix_path_2 = Path(r'/home/dara-shelli/Desktop/password.txt')

place_in_universe = Path()

print(place_in_universe)

user_home = Path.home()
print(user_home)
#/Users/dara-shelli/PycharmProjects/Python
project = Path('/') / 'Users'/'dara-shelli'/'PycharmProjects'/'Python'

print(f'The path {project} exists: {project.exists()}{new_line}')

print(f'The path: {project} is a file: {project.is_file()}')

print(f'The path: {project} is a directory: {project.is_dir()}')

print(project.name)

print(unix_path_1.stem)

print(unix_path_2.suffix)
