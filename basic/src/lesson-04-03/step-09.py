# https://stepik.org/lesson/265082/step/9?unit=246030

red = 'красный'
blue = 'синий'
yellow = 'желтый'
purple = 'фиолетовый'
orange = 'оранжевый'
green = 'зеленый'

color_1, color_2 = input(), input()

if color_1 == color_2:
    if color_1 == red:
        print(red)
    elif color_1 == blue:
        print(blue)
    elif color_1 == yellow:
        print(yellow)
    else:
        print('ошибка цвета')
elif (color_1 == red and color_2 == blue) or (color_1 == blue and color_2 == red):
    print(purple)
elif (color_1 == red and color_2 == yellow) or (color_1 == yellow and color_2 == red):
    print(orange)
elif (color_1 == blue and color_2 == yellow) or (color_1 == yellow and color_2 == blue):
    print(green)
else:
    print('ошибка цвета')
