# https://stepik.org/lesson/334152/step/9?unit=317561

# объявление функции
def is_magic(date):
    date_parts = date.split('.')
    return int(date_parts[0]) * int(date_parts[1]) == int(date_parts[2]) % 100


# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
