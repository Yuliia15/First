a = input("Введите строку:")
def myfuction(a):
    for i in a:
        x = input("Введите символ, который Вы хотите найти в строке:")
        count=a.count(x)
        print("Количество символов в строке: "+str(count))

myfuction(a)


