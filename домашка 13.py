from random import uniform as un
from random import choice
import json


#Треульник

#...
def create_randome_triangle():
    x1, y1 = map(float, (un(-100, 100) for i in range(2)))
    x2, y2 = map(float, (un(-100, 100) for i in range(2)))
    x3, y3 = map(float, (un(-100, 100) for i in range(2)))
    while not trian_sq(x1, y1, x2, y2, x3, y3):
        x3, y3 = map(float, (un(-100, 100) for i in range(2)))
    return x1, y1, x2, y2, x3, y3

#.....
def trian_sq(x1, y1, x2, y2, x3, y3):
    s = ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
    return abs(s) / 2


#...
def create_right_triangle(vert):
    x1, y1 = map(float, vert)
    x2 = x1 + 200. ** 0.5
    y3 = y1 + 200. ** 0.5
    return x1, y1, x2, y1, x1, y3

x1, y1, x2, y2, x3, y3 = create_randome_triangle()
vert = (x1, y1)
print(create_right_triangle(vert))

# Задание 2

#.....
my_join = (''.join([choice('0123456789_') for _ in range(4)]) + ''.join(choice([chr(i) for i in range(ord('a'), ord('z') + 1)]) for _ in range(2)))
print(my_join)

#......

data = {"filename": "filename",
        "Width": "random.randrange(0, 401)",
         "objects":
             [{"class": "1", "xmin": "0", "xmax": "100"},
              {"class": "0", "xmin": "100", "xmax": "200"}]}


with open("D:/tmp_folder/", my_join, "w") as write_file:
    json.dump(data, write_file)


#Неуспешная, очень сонная, реализация создания файла join, я просто оставлю это здесь)
# import json
# from random import choice
#
# def listgen():
#     print()
#     res = ''.join([choice('0123456789_') for _ in range(4)]) + ''.join(choice([chr(i) for i in range(ord('a'), ord('z') + 1)]) for _ in range(2))
#     j = json.dumps(res)
#     print(*j)
#     return res
#
# if __name__ == '__main__':
#     listgen()
