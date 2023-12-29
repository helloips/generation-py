# https://stepik.org/lesson/334150/step/9?unit=317559

# объявление функции
def is_correct_bracket(text):
    while text.find('()') > -1:
        text = text.replace('()', '')
    return len(text) == 0


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
