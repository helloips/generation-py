# https://stepik.org/lesson/328948/step/6?unit=312239

all_texts = list()

for _ in range(int(input())):
    all_texts.append(input())

search_filter = input()

for i in all_texts:
    if search_filter.lower() in i.lower():
        print(i)
