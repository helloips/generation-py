# https://stepik.org/lesson/327207/step/12?unit=310501

n = int(input())
all_el = list()
for _ in range(n):
    all_el.append(int(input()))

del all_el[1::2]

print(all_el)
