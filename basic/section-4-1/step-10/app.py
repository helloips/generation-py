# https://stepik.org/lesson/265081/step/10?unit=246029

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
number_4 = int(input())

if number_1 < number_2 < number_3 < number_4:
    print(number_1)
elif number_2 < number_3 < number_4:
    print(number_2)
elif number_3 < number_4:
    print(number_3)
else:
    print(number_4)
