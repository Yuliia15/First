# Пока While не разлучит нас
def add(a, b, c):
    while a <= b:
        print("Значение a {0} пока что нет".format(a))
        a = a + c
    print("Дождались! Финальный a : {0}".format(a))

a=float(input("Введите число a: "))
b=float(input("Введите число b: "))
c=float(input("Введите число c: "))

add(a, b, c)