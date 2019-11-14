from array import array
from random import randint
import sys
import time

iteration_times = 10
size_msg = 'Size of'
size_unit = 'in bytes'

list_numbers = [randint(0, 1000) for number in range(10_000_000)]
array_numbers = array('i', list_numbers[:])


def get_execution_time(numbers, iterations):
    start_time = time.time()
    for count in range(iterations):
        for number in numbers:
            pass
    else:
        print('--- %s second execution time ---' %(time.time() - start_time), type(numbers))


def print_size(obj):
    print(size_msg, type(obj), sys.getsizeof(obj), size_unit)


get_execution_time(list_numbers, iteration_times)
get_execution_time(array_numbers, iteration_times)

print_size(list_numbers)
print_size(array_numbers)
