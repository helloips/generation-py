# https://stepik.org/lesson/265083/step/12?unit=246031

a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    print('YES')
else:
    print('NO')
