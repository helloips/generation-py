# https://stepik.org/lesson/349846/step/6?unit=333701

from random import choice

ANSWERS = [
    'Бесспорно',
    'Мне кажется - да',
    'Пока неясно, попробуй снова',
    'Даже не думай',
    'Предрешено',
    'Вероятнее всего',
    'Спроси позже',
    'Мой ответ - нет',
    'Никаких сомнений',
    'Хорошие перспективы',
    'Лучше не рассказывать',
    'По моим данным - нет',
    'Определённо да',
    'Знаки говорят - да',
    'Сейчас нельзя предсказать',
    'Перспективы не очень хорошие',
    'Можешь быть уверен в этом',
    'Да',
    'Сконцентрируйся и спроси опять',
    'Весьма сомнительно'
]


def predict():
    _ = input('Задайте вопрос...\n')
    print(choice(ANSWERS))


def say_hello():
    name = input('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос. Как тебя зовут?\n')
    print('Привет,', name)


def say_goodbye():
    print('Хочешь задать ещё вопрос? просто скажи "да"')
    if input().lower() == 'да':
        return True
    else:
        print('Возвращайся, если возникнут вопросы!')
        return False


say_hello()
have_questions = True
while have_questions:
    predict()
    have_questions = say_goodbye()
