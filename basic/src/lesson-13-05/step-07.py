# https://stepik.org/lesson/334150/step/7?unit=317559

# объявление функции
def is_palindrome(text):
    actual_chars = [i.upper() for i in text if i.isalpha()]
    return actual_chars == actual_chars[::-1]


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
