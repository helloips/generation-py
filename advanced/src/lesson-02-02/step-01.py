# https://stepik.org/lesson/415554/step/1?unit=405083

def extract_xy_from_input():
    raw_xy = input()
    xy = raw_xy.split(' ')
    return int(xy[0]), int(xy[1])


first, second, third, fourth = 0, 0, 0, 0

n = int(input())
for _ in range(n):
    x, y = extract_xy_from_input()
    if x > 0 and y > 0:
        first += 1
    elif x < 0 and y > 0:
        second += 1
    elif x < 0 and y < 0:
        third += 1
    elif x > 0 and y < 0:
        fourth += 1

print('Первая четверть:', first)
print('Вторая четверть:', second)
print('Третья четверть:', third)
print('Четвертая четверть:', fourth)
