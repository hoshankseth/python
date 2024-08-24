
range_onetofive = [num *2 for num in range(1,5)]

print(range_onetofive)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

short_list = [name for name in names if len(name) <5]

print(short_list)

uppercase_list = [name.upper() for name in names if len(name) > 5]

print(uppercase_list)

import numpy as np

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

sq_numbers = [np.square(num) for num in numbers]

print(sq_numbers)


even_num = [num for num in numbers if num % 2 ==0b   ]
print(even_num)