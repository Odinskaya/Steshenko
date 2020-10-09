# Задача 1

number = "10203040506070"
symbol = "0"
count = number.count(symbol)
print(count)

# Задача 2

value = 507607000
count = 0
while value % 10 == 0:
    count += 1
    value //= 10
print(count)


# Задача 3

my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [10, 15, 20, 25]
my_result = [x for x in my_list_1 if not x % 2] + [x for x in my_list_2 if x % 2]
print(my_result)

# Задача 4

my_list = [1, 2, 3, 4]
my_list[0], my_list[3] = my_list[3], my_list[0]
new_list = my_list
print(new_list)

# Задача 5

my_list = [1, 2, 3, 4]
my_list.append(1)
my_list.pop(0)
print(my_list)

# Задача 6

str_ = "66 больше чем 44 но меньше чем 22"
str_ = [int(s) for s in str_.split() if s.isdigit()]
res = 0
for i in str_:
    res += i
print(res)

# Задача 7

my_str ='gfdsqgze'
print(list(map(''.join, zip(*[iter(my_str + '_')]*2))))

# Задача 8

# Задача 9

# Задача 10

str_my = [2, 4, 1, 5, 3, 9, 0, 7]
print(sum([str_my[i - 1] < str_my[i] > str_my[i+1] for i in range(1, len(str_my) - 1)]))

