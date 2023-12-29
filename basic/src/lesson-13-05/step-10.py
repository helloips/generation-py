# https://stepik.org/lesson/334150/step/10?unit=317559

# объявление функции
def convert_to_python_case(text):
    result = list()
    for i in text:
        if i.isupper():
            result.append('_')
        result.append(i.lower())
    return ''.join(result[1:])


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
