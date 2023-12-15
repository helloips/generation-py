# https://stepik.org/lesson/328948/step/5?unit=312239

n = int(input())
uniq_words = list()

for _ in range(n):
    current_word = input()
    if current_word not in uniq_words:
        uniq_words.append(current_word)

print(*uniq_words, sep="\n")
