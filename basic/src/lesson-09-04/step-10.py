# https://stepik.org/lesson/303083/step/10?unit=284990

n = int(input())
count = 0

for _ in range(n):
    text = input()
    if text.count("11") >= 3:
        count += 1

print(count)
