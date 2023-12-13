# https://stepik.org/lesson/327207/step/14?unit=310501

result = list()

for _ in range(int(input())):
    current = input()
    result.extend([c for c in current])

print(result)
