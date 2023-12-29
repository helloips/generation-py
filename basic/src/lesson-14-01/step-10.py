# https://stepik.org/lesson/334152/step/10?unit=317561

# объявление функции
def is_pangram(text):
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if text.upper().count(i) == 0:
            return False
    else:
        return True


# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
