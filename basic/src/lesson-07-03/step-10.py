# https://stepik.org/lesson/294243/step/10?unit=275922

result = 1

for _ in range(10):
    number = int(input())
    result = result * number if number != 0 else result

print(result)
