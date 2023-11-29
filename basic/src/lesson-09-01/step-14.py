# https://stepik.org/lesson/284101/step/14?unit=265440

text = input()
vowels = 0
consonants = 0

for i in text:
    if i.lower() in ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']:
        vowels += 1
    elif i.lower() in ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']:
        consonants += 1

print('Количество гласных букв равно', vowels)
print('Количество согласных букв равно', consonants)
