value = 50
new_value = value // 2 if value < 100 else -value
print (new_value)

#####################################################

value = 50
new_value = value = 1 if value < 100 else 0
print (new_value)

#####################################################

value = 50
new_value = True if value < 100 else False
print (new_value)

#####################################################

my_str = "Пираты Карибского моря 2: Сундук Мертвеца"
if my_str.upper:
    print (my_str.upper())

#####################################################

my_str = "ГАРРИ ПОТТЕР И ТАЙНАЯ КОМНАТА"
if my_str.lower:
    print (my_str.lower())

#####################################################

my_str = "Пони"
if len(my_str) < 5:
    print (my_str + my_str)
else:
    print (my_str)

#####################################################

my_str = "ХИРО"
if len(my_str) < 5:
    print(my_str + my_str[::-1])
else:
    print (my_str)

#####################################################

my_str = "У меня есть 5 яблок и 4 мандарина"
print(''.join(x for x in my_str if x.isalnum()))

#####################################################

my_str = "Я_прочитал_100_книг"
print (''.join(x for x in my_str if not x.isalnum()))

#####################################################

string = "**ст&рок/а"
for symbol in string:
    if not symbol.isalnum():
        print(symbol, end=" ", flush=True)
