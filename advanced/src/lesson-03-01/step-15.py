# https://stepik.org/lesson/440563/step/15?unit=430761

# объявление функции
def func(num1, num2):
    return num1 % num2 == 0


# считываем данные
num1, num2 = int(input()), int(input())

# вызываем функцию
if func(num1, num2):
    print("делится")
else:
    print("не делится")
