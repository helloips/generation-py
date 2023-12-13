# https://stepik.org/lesson/327207/step/11?unit=310501

n = int(input())
result = list()

prev = int(input())
for _ in range(n - 1):
    current = int(input())
    result.append(prev + current)
    prev = current

print(result)
