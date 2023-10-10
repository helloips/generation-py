# https://stepik.org/lesson/311433/step/4?unit=293861

mx = -10 ** 7
s = 0
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
        if x > mx:
            mx = x
if s >= 0:
    print('NO')
else:
    print(s)
    print(mx)
