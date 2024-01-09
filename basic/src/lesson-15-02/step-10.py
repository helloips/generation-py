# https://stepik.org/lesson/349845/step/10?unit=333700

import random


def start_game(max_number):
    secret_number = random.randint(1, max_number)
    attempts = list()
    print('Введите Ваш вариант от', 1, 'до', max_number)
    while True:
        attempt = convert_or_default(input(), -1)
        if is_valid(attempt, max_number):
            if attempt > secret_number:
                attempts.append(attempt)
                print('Ваше число больше загаданного, попробуйте еще разок')
            elif attempt < secret_number:
                attempts.append(attempt)
                print('Ваше число меньше загаданного, попробуйте еще разок')
            else:
                attempts.append(attempt)
                print('Вы угадали, поздравляем! Попыток:', len(attempts))
                break
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')


def say_hello():
    print('Добро пожаловать в числовую угадайку! Пожалуйста, установите границу для загадывания')
    return convert_or_default(input(), 100)


def say_goodbye():
    print('Спасибо, что играли в числовую угадайку. Повторим?')
    if input().lower() == 'y':
        play()


def is_valid(attempt, max_number):
    return True if 1 <= attempt <= max_number else False


def convert_or_default(raw_text, default_number):
    return int(raw_text) if raw_text.isdigit() else default_number


def play():
    start_game(say_hello())
    say_goodbye()


play()
