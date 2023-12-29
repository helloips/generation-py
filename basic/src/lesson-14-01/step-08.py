# https://stepik.org/lesson/334152/step/8?unit=317561

# объявление функции
def get_month(language, number):
    ru_names = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
                'ноябрь', 'декабрь']
    en_names = ['', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                'november', 'december']
    if language == 'ru':
        return ru_names[number]
    elif language == 'en':
        return en_names[number]
    else:
        return ''


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
