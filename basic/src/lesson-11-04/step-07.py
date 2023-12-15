# https://stepik.org/lesson/328948/step/7?unit=312239

all_texts = list()
search_filters = list()

for _ in range(int(input())):
    all_texts.append(input())

for _ in range(int(input())):
    search_filters.append(input())

for i in all_texts:
    is_contains = True
    for u in search_filters:
        if u.lower() not in i.lower():
            is_contains = False
            break
    if is_contains:
        print(i)
