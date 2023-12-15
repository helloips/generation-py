# https://stepik.org/lesson/328948/step/8?unit=312239

negatives = list()
zeros = list()
positives = list()

for _ in range(int(input())):
    current = int(input())
    if current < 0:
        negatives.append(current)
    elif current == 0:
        zeros.append(current)
    else:
        positives.append(current)

print(*negatives, sep='\n')
print(*zeros, sep='\n')
print(*positives, sep='\n')
