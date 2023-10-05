# https://stepik.org/lesson/294243/step/12?unit=275922

n = int(input())
result = 0

is_adding = True
for i in range(1, n + 1):
    result += i if is_adding else - i
    is_adding = not is_adding

print(result)
