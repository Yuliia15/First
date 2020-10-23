#Создать функцию, которая будет случайным образом генерировать два списка случайным образом
#после чего сравнивать элементы этих двух списков и выводить в консоль новый список
#который будет состоять из элементов, которые есть в обоих оригинальных списках

import random

a =[random.randint(1,20) for i in range(10)]
print(a)
b = [random.randint(1, 20) for i in range(10)]
print(b)
new_list = []
for element in a:
    if element in b:
        new_list.append(element)
print(new_list)