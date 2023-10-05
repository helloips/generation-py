# https://stepik.org/lesson/265082/step/7?unit=246030

weight = int(input())

if weight < 60:
    print('Легкий вес')
elif 60 <= weight < 64:
    print('Первый полусредний вес')
elif 64 <= weight < 69:
    print('Полусредний вес')
