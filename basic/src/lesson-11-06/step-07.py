# https://stepik.org/lesson/324754/step/7?unit=307930

text = input()
articles = ['a', 'an', 'the', 'A', 'An', 'The']

count = 0
for i in text.split():
    if i in articles:
        count += 1

print('Общее количество артиклей:', count)
