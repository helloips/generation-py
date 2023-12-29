# https://stepik.org/lesson/327221/step/3?unit=310520

words = input().split()
numbers = [int(i) for i in words]
print('+'.join(words), '=', sum(numbers), sep='')
