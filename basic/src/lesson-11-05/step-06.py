# https://stepik.org/lesson/324755/step/6?unit=307931

text = input()
values = text.split()

for i in values:
    digit = int(i)
    print(digit * '+')
