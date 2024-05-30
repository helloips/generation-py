# https://stepik.org/lesson/416753/step/8?unit=406261

n = int(input())

for i in range(n):
    current_list = list()
    for j in range(n):
        current_list.append(j + 1)
    print(current_list)
