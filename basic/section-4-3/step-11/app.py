# https://stepik.org/lesson/265082/step/11?unit=246030

a_1, b_1, a_2, b_2 = int(input()), int(input()), int(input()), int(input())

if a_2 <= a_1 <= b_2:
    if b_1 <= b_2:
        print(a_1, b_1)
    elif a_1 == b_2:
        print(a_1)
    else:
        print(a_1, b_2)
elif a_1 <= a_2 <= b_1:
    if b_2 <= b_1:
        print(a_2, b_2)
    elif a_2 == b_1:
        print(a_2)
    else:
        print(a_2, b_1)
else:
    print('пустое множество')
