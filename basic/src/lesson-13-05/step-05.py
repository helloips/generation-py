# https://stepik.org/lesson/334150/step/5?unit=317559

# объявление функции
def is_password_good(password):
    if len(password) >= 8 \
            and not password.islower() \
            and not password.isupper() \
            and len([i for i in password if i.isdigit()]) > 0 \
            and len([i for i in password if i.isalpha()]) > 0:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
