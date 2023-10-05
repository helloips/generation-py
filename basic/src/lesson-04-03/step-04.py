# https://stepik.org/lesson/265082/step/4?unit=246030

a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print('Равносторонний')
elif a == b or b == c or c == a:
    print('Равнобедренный')
else:
    print('Разносторонний')
