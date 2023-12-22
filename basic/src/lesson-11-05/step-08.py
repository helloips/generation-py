# https://stepik.org/lesson/324755/step/8?unit=307931

text = input()
separator = input()
result = list()

for i in text:
    result.append(i)
    result.append(separator)

print(''.join(result[:-1]))
