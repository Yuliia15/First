def function1():
    print("Hello")
    print("Hello2")
print("Hello from outside")
function1()

def function2(x):
     return 2*x
a = function2(5)
print(a)
def sum_of_two_numbers(x, y):
    return x + y
e = sum_of_two_numbers(4,5)
print(e)

def function5(some_argument):
    print(some_argument)
    print("hello")
function5(5)
a = function5(5)

def function6():
    return 5
print(function6())
a = function6()
print(a)
a = function5(123)
print(a)

def function7(x):
    print(x)
    print("hi")
    return 3*x
a = function7(10)
print(a)

name1 = "Tom"
height1 = 1.90
weight1 = 80

name2 = "Katy"
height2 = 1.70
weight2 = 60

name3 = "Bob"
height3 = 2
weight3 = 150

def bmi_calculator(name, height, weight):
    bmi = weight / (height**2)
    print("Индекс массы тела " + str(bmi))

    if bmi < 25:
        return name + " не имеет лишнего веса"
    else:
        return name + " имеет лишний вес"
bmi1 = bmi_calculator(name1, height1, weight1)
bmi2 = bmi_calculator(name2, height2, weight2)
bmi3 = bmi_calculator(name3, height3, weight3)
print(bmi1)
print(bmi2)
print(bmi3)

miles = 5
km = 1.609
def convert(miles):
    convert1 = miles * km
    print("В 5 миль " + str(convert1) + " км")

convert = convert(miles)
print(convert)


def convert_of_miles(a, b):
    return a * b



c = convert_of_miles(1, 1.609)
print("В 1 миле " + str(c) + " км")

# площадь прямоугольника
def area(lenght, height):
    return lenght * height
a = area(5,10)
print("Площадь прямоугольника составляет " + str(a))

sec=6000;
a=int(sec/60);
print(a);

for b in range(a):
        print(b,a)
        if b == 60:
            c = 1
            d = a-b

print ("dney:","chasov:",c,"minut:",d, "sekund:" );