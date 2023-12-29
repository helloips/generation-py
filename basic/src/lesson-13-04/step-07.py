# https://stepik.org/lesson/331754/step/7?unit=315133

# объявление функции
def get_days(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 28
    else:
        return 0


# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))
