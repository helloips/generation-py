# https://stepik.org/lesson/415553/step/3?unit=405082

weight = float(input())
height = float(input())

BMI = weight / (height * height)

if 18.5 <= BMI <= 25:
    print('Оптимальная масса')
elif 18.5 > BMI:
    print('Недостаточная масса')
else:
    print('Избыточная масса')
