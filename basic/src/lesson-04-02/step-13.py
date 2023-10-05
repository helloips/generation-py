# https://stepik.org/lesson/265083/step/13?unit=246031

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('YES')
else:
    print('NO')
