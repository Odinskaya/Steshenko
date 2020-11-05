from random import randint
import io
import chardet
import os
import codecs
import random
from re import match

with open("C:/Users/user/Desktop/Python/domains.txt", "r") as name:
    text = name.read()
    domen_name = text.replace(".", "")
    domen_name_1 = domen_name.split("\n")

with open("C:/Users/user/Desktop/Python/names.txt", "r") as name1:
    surnames = '\n'.join([line.split()[1] for line in name1.readlines()])
    surnames_1 = surnames.split("\n")

random_number = random.randint(100, 1000)
random_word = ''.join(chr(randint(ord('a'), ord('z'))) for j in range(randint(5, 7)))

print("".join(random.choice(surnames_1) + "." + str(random_number) + "@" + str(random_word) + "." + random.choice(domen_name_1)))




