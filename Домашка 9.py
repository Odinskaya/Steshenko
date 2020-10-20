import os
import time
import sys

#Задача экспресс

def myfunc(s):
    result = {}
    path = os.path.abspath(s)
    if os.path.exists(path):
        dirs = []
        files = []
        for e in os.listdir(path):
            if os.path.isdir(os.path.join(path, e)):
                dirs.append(e)
            else:
                files.append(e)
        result["dirs"] = dirs[:]
        result["files"] = files[:]
    return result

print(myfunc("./temp/"))

#Задача 1

#Вариант 1
with open("D:\pythonProject/authors.txt", "r") as text_:
    for record in text_:
        step1 = record.split("", 4)
        step2 = step1[4].split("'s ", 2)
        step3 = step2[1].split(",", 2)
        print(step1[0], step1[1], step1[2], step3[0].lower())

#Вариант 2
with open("D:\pythonProject/authors.txt", "r") as f:
    for s in f:
       if len(s.split()) > 1:
           s = s.split(" - ")
       print(s[0], s[1].split(",")[0].split()[-1].lower())

# Вариант 3

with open("authors.txt", "rt", encoding="utf-8") as file:
    for line in file:
        data, info = line.split("-")
        action = "birthday" if "birthday" in info else "death"
        print(data, action)

# Задача 2

with open("D:\pythonProject/authors.txt", "r") as file:
    for line in file:
        date, info = line.split("-")
        name = info.split(",")[0]
        d, m, y = date.split()
        name_ = {"name": name, "date": date}
        print(name_)


# Задача 3

with open("D:\pythonProject/authors.txt", "r") as file:
    for line in file:
        date, info = line.split('-')
        name = info.split(',')[0]
        date = '/'.join(date.split())
        name_ = {"name": name, "date": date}
        print(list(map(name_.splitlines())))
