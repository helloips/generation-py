# https://stepik.org/lesson/328948/step/3?unit=312239

n = int(input())
in_values = list()

for _ in range(1, n + 1):
    in_values.append(int(input()))

print(*in_values, sep="\n")
print()
print(*[i ** 2 + 2 * i + 1 for i in in_values], sep="\n")
