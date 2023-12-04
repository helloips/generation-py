# https://stepik.org/lesson/324750/step/9?unit=307926

n = int(input())

a_ord = ord("a")
result = list()

for i in range(a_ord, a_ord + n):
    result.append(chr(i))

print(result)
