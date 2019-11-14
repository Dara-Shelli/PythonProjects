course = 'Python Programming'

course_upper = course.upper()
course_lower = course.lower()

first_name = 'Dara-Shelli'
last_name = 'Tvisher'

full_name = F'{first_name} {last_name}'.title()
print(full_name)

course_excess_whitespaces = '               course'


# Left trim

course_fixed_left = course_excess_whitespaces.lstrip()


print(course.find('Pro'))


course_replaced_chars = course.replace('o', 'O')
print(course_replaced_chars)

print('Python' in course)
print('Python ' not in course)
