# https://stepik.org/lesson/327207/step/10?unit=310501

n = int(input())
result = list()

for i in range(1, n + 1):
    if n % i == 0:
        result.append(i)

print(result)
