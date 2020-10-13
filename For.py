from random import randint
a = [randint(0, 10) for i in range(5)]
print(a)
b=int((input('Vvvvведите число из списка: ')))
if b in a:
   # n=a.index(b) + 1
   # c='Ваша цифра под номером: '+ str(n)
    print('Ваша цифра под номером:' + str(a.index(b)+1))