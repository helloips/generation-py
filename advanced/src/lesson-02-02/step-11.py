# https://stepik.org/lesson/415554/step/11?unit=405083

SUFFIX = 'запретил букву'
DELIMITER = ' '
ALPHABET = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
            'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
            'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

word = input()
song_words = word + DELIMITER + SUFFIX

for alpha in ALPHABET:
    if song_words.find(alpha) != -1:
        print(song_words + DELIMITER + alpha)
        song_words = song_words.replace(alpha, '')
        song_words = song_words.replace(DELIMITER + DELIMITER, DELIMITER)
        song_words = song_words.rstrip().lstrip()
