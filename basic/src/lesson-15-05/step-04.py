# https://stepik.org/lesson/352860/step/4?unit=336821


ENG_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
RUS_ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def get_actual_char(source, position, is_upper):
    actual_char = source[position]
    return actual_char.upper() if is_upper else actual_char.lower()


def encrypt(step, source, target):
    encrypted_text = ''
    for i in target:
        if i.isalpha():
            position = source.index(i.upper())
            encrypted_position = (position + step) % len(source)
            encrypted_text = encrypted_text + get_actual_char(source, encrypted_position, i.isupper())
        else:
            encrypted_text += i
    return encrypted_text


def decrypt(step, source, target):
    decrypted_text = ''
    for i in target:
        if i.isalpha():
            position = source.index(i.upper())
            decrypted_position = (position - step) % len(source)
            decrypted_text = decrypted_text + get_actual_char(source, decrypted_position, i.isupper())
        else:
            decrypted_text += i
    return decrypted_text


def caesar_answer_me(action, language, step, text):
    if language == 'eng':
        source = ENG_ALPHABET
    elif language == 'rus':
        source = RUS_ALPHABET
    else:
        source = ''

    if action == 'encrypt':
        return encrypt(step, source, text)
    elif action == 'decrypt':
        return decrypt(step, source, text)
    else:
        return ''


user_action = input('Укажите тип действия (encrypt/decrypt): ').lower()
user_language = input('Укажите язык (eng/rus): ').lower()
user_step = int(input('Укажите размер сдвига: '))
user_text = input('Введите текс для обработки: ')

result = caesar_answer_me(user_action, user_language, user_step, user_text)

print(result)
