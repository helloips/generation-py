# https://stepik.org/lesson/326725/step/11?unit=310010

print(*[int(i) ** 2 for i in input().split() if int(i) % 2 == 0 and str(int(i) ** 2)[-1] != '4'])
