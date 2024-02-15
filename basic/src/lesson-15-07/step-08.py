# https://stepik.org/lesson/349847/step/8?unit=333702

import random

WORD_LIST = ['Питон', 'что', 'за', 'заварушка']


def get_word():
    return random.choice(WORD_LIST).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)
    print()

    while not guessed and tries > 0:
        user_guess = input('Введите букву или слово: ').upper()
        if len(user_guess) == 1 and user_guess.isalpha():
            if user_guess in guessed_letters:
                print('Вы уже называли букву', user_guess)
            elif user_guess not in word:
                print('Буквы', user_guess, 'нет в слове.')
                tries -= 1
                guessed_letters.append(user_guess)
            else:
                print('Отличная работа, буква', user_guess, 'присутствует в слове!')
                guessed_letters.append(user_guess)
                word_as_list = list(word_completion)
                indices = [i for i in range(len(word)) if word[i] == user_guess]
                for index in indices:
                    word_as_list[index] = user_guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(user_guess) == len(word) and user_guess.isalpha():
            if user_guess in guessed_words:
                print('Вы уже называли слово', user_guess)
            elif user_guess != word:
                print('Слово', user_guess, 'не является верным.')
                tries -= 1
                guessed_words.append(user_guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Введите букву или слово.')
        print(display_hangman(tries))
        print(word_completion)
        print()
    if guessed:
        print('Поздравляем, вы угадали слово! Вы победили!')
    else:
        print('Вы не угадали слово. Загаданным словом было ' + word + '. Может быть в следующий раз!')


again = 'д'

while again.lower() == 'д':
    word = get_word()
    play(word)
    again = input('Играем еще раз? (д = да, н = нет):')
