# https://stepik.org/lesson/327207/step/13?unit=310501

words = list()
for _ in range(int(input())):
    words.append(input())

k = int(input())

for word in words:
    if k <= len(word):
        print(word[k - 1], end='')
