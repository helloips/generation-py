# https://stepik.org/lesson/324755/step/7?unit=307931

ip = input()
parts = ip.split(".")

for i in parts:
    digit = int(i)
    if digit < 0 or digit > 255:
        print('НЕТ')
        break
else:
    print('ДА')
