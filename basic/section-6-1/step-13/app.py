# https://stepik.org/lesson/265105/step/13?unit=246053

n_1, n_2, n_3 = int(input()), int(input()), int(input())

n_max = max(n_1, n_2, n_3)
n_min = min(n_1, n_2, n_3)
n_middle = n_1 + n_2 + n_3 - n_max - n_min

print(n_max)
print(n_middle)
print(n_min)
