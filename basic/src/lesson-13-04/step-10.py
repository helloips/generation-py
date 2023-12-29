# https://stepik.org/lesson/331754/step/10?unit=315133

# объявление функции
def find_all(target, symbol):
    indexes = list()

    for i in range(0, len(target)):
        if target[i] == symbol:
            indexes.append(i)

    return indexes


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
