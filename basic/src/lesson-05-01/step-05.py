# https://stepik.org/lesson/292172/step/5?unit=273659

number = int(input())

if number % 2 != 0:
    print('YES')
else:
    if 2 <= number <= 5 or number > 20:
        print('NO')
    elif 6 <= number <= 20:
        print('YES')
