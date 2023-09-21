# https://stepik.org/lesson/265083/step/11?unit=246031

number = int(input())

if 1 <= number / 1000 < 10 and (number % 7 == 0 or number % 17 == 0):
    print('YES')
else:
    print('NO')
