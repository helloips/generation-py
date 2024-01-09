# https://stepik.org/lesson/349848/step/6?unit=333703

from random import choice

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
AMBIGUOUS_CHARACTERS = 'il1Lo0O'


def generate_password(length, chars):
    if len(chars) == 0:
        return ''
    password = ''
    for _ in range(length):
        password += choice(chars)
    return password


acceptable_chars = ''

print("Введите требования к паролю")
password_count = int(input('Количество паролей для генерации: '))
password_length = int(input('Длину одного пароля: '))
if input('Включать ли цифры? (y/n): ').lower().strip() == 'y':
    acceptable_chars += DIGITS
if input('Включать ли прописные буквы? (y/n): ').lower().strip() == 'y':
    acceptable_chars += LOWERCASE_LETTERS
if input('Включать ли строчные буквы? (y/n): ').lower().strip() == 'y':
    acceptable_chars += UPPERCASE_LETTERS
if input('Включать ли символы? (!#$%&*+-=?@^_) (y/n): ').lower().strip() == 'y':
    acceptable_chars += PUNCTUATION
if input('Исключать ли неоднозначные символы? (il1Lo0O) (y/n): ').lower().strip() == 'y':
    for c in AMBIGUOUS_CHARACTERS:
        acceptable_chars = acceptable_chars.replace(c, '')

for _ in range(password_count):
    print(generate_password(password_length, acceptable_chars))
