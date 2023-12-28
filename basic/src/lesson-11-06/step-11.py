# https://stepik.org/lesson/324754/step/11?unit=307930

numbers = [int(i) for i in input().split()]

numbers.sort(reverse=False)
print(*numbers)
numbers.sort(reverse=True)
print(*numbers)
