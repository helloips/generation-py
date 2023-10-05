# https://stepik.org/lesson/265081/step/11?unit=246029

age = int(input())

if age <= 13:
    print('детство')
elif 14 <= age <= 24:
    print('молодость')
elif 25 <= age <= 59:
    print('зрелость')
else:
    print('старость')
