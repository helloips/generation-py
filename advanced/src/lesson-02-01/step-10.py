# https://stepik.org/lesson/415553/step/10?unit=405082

n = int(input())
k = int(input())

skip = k - 1
index = skip
survivors = list(range(1, n + 1))
while len(survivors) > 1:
    survivors.pop(index)
    index = (index + skip) % len(survivors)

print(survivors[0])
