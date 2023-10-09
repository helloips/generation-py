# https://stepik.org/lesson/298794/step/7?unit=280621

number = int(input())

for i in range(2, number + 1):
    if number % i == 0:
        print(i)
        break
