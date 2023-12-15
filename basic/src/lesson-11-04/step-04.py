# https://stepik.org/lesson/328948/step/4?unit=312239

n = int(input())
in_values = list()

for _ in range(n):
    current = int(input())
    in_values.append(current)

del in_values[in_values.index(min(in_values))]
del in_values[in_values.index(max(in_values))]

print(*in_values, sep="\n")
