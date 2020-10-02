# 1 задача
my_list = [10, 40, 110, 140, 150, 160]
for elem in my_list:
    if elem > 100:
      print(elem)

#####################################################
# 2 задача
my_list = [10, 40, 220, 270, 280, 290]
my_results = []
for i in my_list:
    if i > 100:
       my_results.append(i)
for i in my_results:
    print(i)

#####################################################

# 3 задача
my_list = [300, 400, 500]
def func(my_list):
   if len(my_list) < 2:
        my_list.append(0)

   elif len(my_list) >= 2:
        my_list.append(my_list[-1]+my_list[-2])
   return my_list
if __name__ == "__main__":
    func(my_list=([1,2,3]))
print(func(my_list))
#####################################################

# 4 задача

try:
    print(float(input("Введи не целое число: "))**-1)
except:
     print("Введены не цифры!")

#####################################################

# 5 задача
my_list = [0, 10, 50, 70, 540, 650]
my_index = [0, 1, 2, 3, 4, 5]
print(*[my_list[i] for i in my_index], sep = ", ")

#####################################################

# 6 задача
my_list_1 = [1, 3]
my_list_2 = [2, 4]
my_index = [x for x in range(0, len(my_list_1))]
for i in my_index:
    print((my_list_1[i], my_list_2[i]))

#####################################################

# 7 задача
my_string = '0123456789'
output_list = []

for i in my_string:
    for j in my_string:
      output_list.append(int(f"{i}{j}"))

print(output_list)