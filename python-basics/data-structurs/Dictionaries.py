new_line ='\n'

first_key = 'x'
second_key = 'y'
third_key = 'z'
invalid_key = 'invalid key'

msg_z = 'The value of z is: '
mem_loc_msg = 'memory location: '

first_point = {first_key: 1, second_key: 2}

sec_point = dict(x=1, y=2)

print(f'{first_point} {mem_loc_msg} {id(first_point)}')
print(f'{sec_point} {mem_loc_msg} {id(sec_point)}')

first_point[first_key] = 5
first_point[third_key] = 14

print(f'{msg_z} {first_point["z"]}', new_line)
