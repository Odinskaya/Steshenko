import random
from random import randint
import csv
import json
import string



# Задача 1

def open_txt_for_write():
    global text
    file_name = "your.txt"
    f = open(file_name, "w")
    f.write(f"{text}\n\n\n\n\n\n\n\n\n")
    f.close()
def buildblock():
    size = random.randint(100, 1000)
    out_str = ""
    for i in range(0, size):
      a = random.randint(65, 90)
      out_str += chr(a)
      return(out_str)
      open_txt_for_write()

# Задача 2

def read_json(filename_with_path):
    global json
    file_name = "your.json"
    f = open(file_name, "w")
    data = json.load(file_name)
    data_1 = random.randint("".join(chr(randint(ord('a'), ord('z'))) for j in range(5)))
    data_2 = random.randint(-100, 100)
    name = [{data_1 : data_2} for i in range(randint(5, 20))]
    print(*name, sep='\n')

# Задача 3

def write_file(filename:""):
    with open("mytext.csv", "w", newline="") as csv_file:
       spamwriter = csv.writer(csv_file, delimiter=';')
       n = random.randint(3, 10)
       m = random.randint(3, 10)
       spamwriter.writerow(n)
       spamwriter.writerow(m)

#

with open("Python/test_write.json") as json_file:
    def outfile(filename_with_path, mode: str):
      if mode == "txt":
         data = read_txt(filename_with_path)
      elif mode == "json":
         data = read_json(filename_with_path)
      elif mode == "csv":
         data = read_csv(filename_with_path)
      else:
         raise Exception("Unsupported file format!")
       return data

something = outfile("test_write.json", "json")
print(something)