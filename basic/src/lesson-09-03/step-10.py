# https://stepik.org/lesson/296416/step/10?unit=278136

text = input()

position = text.lower().find('хорош')

print('YES' if position > -1 else 'NO')
