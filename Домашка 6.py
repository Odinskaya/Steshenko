# Задача 1

my_list = ["cat", "dog", "python", "book", "manga"]
newlist_1 = [x[::-1] if i % 2 else x for i, x in enumerate(my_list)]
print(newlist_1)

# Задача 2

my_list = ["абракадабра", "книга", "абзац", "море"]
newlist_2 = [i for i in my_list if i[0] == "а"]
print(newlist_2)

# Задача 3

my_list = ["абракадабра", "мемчик", "абзац", "море", "бровь", "альфей"]
newlist = [newlist for newlist in my_list if "а" in newlist]
print(newlist)

# Задача 4

# ~ Вариант 1
my_list = ["str", 4, 5, "shrek", "home", 5, 22, "prince"]
new_my_list = []
for i in range(len(my_list)):
    if not str(my_list[i]).isdigit():
        new_my_list.append(my_list[i])
print(new_my_list)

# ~ Вариант 2

my_list_2 = ["str", 4, 5, "shrek", "home", 5, 22, "prince"]
new_my_list_2 = [i for i in my_list if not str(i).isdigit()]
print(new_my_list_2)

# Задача 5

my_str = "это только моя строка"
mylist_1 = []
for i in my_str:
    if my_str.count(i) == 1:
        mylist_1.append(i)
print(mylist_1)

# Задача 6

s1 = "asdfqwqasdsfq"
s2 = "qwerzxa"

listmy = list(set(s1) & set(s2))
print(listmy)

# Задача 7

str1_ = "Гарри Поттер и Филосовский камень"
str2_ = "Гарри Поттер и Тайная комната"
res = []
for i in str1_:
    k = str1_.find(i) - str1_.rfind(i)
    if k == 0:
        if i in str2_ and str2_.find(i) - str2_.rfind(i) == 0:
            print(i)
            res.append(i)

# Задача 8

person = {"name": "Вика",
          "surname": "Стешенко",
          "age": 22,
          "country of residence": "Украина",
          "city": "Днепр",
          "work": True}
print(person)

# Задача 9

tort = {"Коржи":
            {"Мука": "4 стакана муки",
             "Молоко": "250мл молока",
             "Масло": "пол пачки масла",
             "Яйцо": "2 яйца"},
        "Крем":
            {"Сахар": "3 ложки сахара",
             "Масло": "пачка масла",
             "Ваниль": "10 грамм ванильного сахара",
             "Сметана": "пачка сметаны"},
        "Глазурь":
            {"Какао": "300гр какао порошка",
             "Сахар": "пол стакана сахара",
             "Масло": "пол пачки масла"}}

print(tort["Крем"])
# В print пишем, какой именно раздел нам нужен, или же вот так: print(tort["Коржи"]["Мука"]),
# и узнаем конкретно ещё и по ингредиентам)


