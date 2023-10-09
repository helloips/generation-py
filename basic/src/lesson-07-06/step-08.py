# https://stepik.org/lesson/298794/step/8?unit=280621

number = int(input())

for i in range(1, number + 1):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i)
