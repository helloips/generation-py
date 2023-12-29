# https://stepik.org/lesson/334150/step/6?unit=317559

# объявление функции
def is_one_away(word1, word2):
    return len(word1) == len(word2) \
           and word1 != word2 \
           and len([i for i in range(0, len(word1)) if word1[i] != word2[i]]) == 1


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))
