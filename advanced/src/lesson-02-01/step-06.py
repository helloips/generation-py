# https://stepik.org/lesson/415553/step/6?unit=405082

YEAR_NAMES = [
    'Петух',
    'Собака',
    'Свинья',
    'Крыса',
    'Бык',
    'Тигр',
    'Заяц',
    'Дракон',
    'Змея',
    'Лошадь',
    'Овца',
    'Обезьяна',
]

year = int(input())
count = len(YEAR_NAMES)

actual_index = year % count

print(YEAR_NAMES[actual_index - 1])
