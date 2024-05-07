# https://stepik.org/lesson/415554/step/4?unit=405083

numbers = list(int(i) for i in input().split(' '))

print(numbers[-1], *numbers[0:-1:])
