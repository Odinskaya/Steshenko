# Задача 1

from random import randint
numbers = []
for i in range(20):
    numbers.append(randint(1, 101))
print(numbers)

# Задача 2

from random import uniform as ru
triangle = {x: [ru(1, 10.0), ru(1, 10.0)] for x in ["A","B", "C"]}
print(triangle)

# Задача 3

my_str = "Im the string"
def func (my_str):
    print("***" + my_str + "***")
func(my_str)

# Задача 4

my_dict_1 = {"a":1, "b":2, "c":3, "d":4, "e":5}
my_dict_2 = {"f":6, "a":7, "g":8, "b":9, "h":10}

# a
print(list(my_dict_1.keys() & my_dict_2.keys()))

# б
print(list(my_dict_1.keys() - my_dict_2.keys()))

# в
my_dict_3 = dict(i for i in my_dict_1.items() if i[0] not in my_dict_2.keys())
print(my_dict_3)

# г 
my_dict_2.update(my_dict_1)
print(my_dict_2)


