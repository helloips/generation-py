# https://stepik.org/lesson/327207/step/8?unit=310501

result = list()

for i in range(ord('a'), ord('a') + 26):
    result.append(chr(i) * (i - 96))

print(result)
