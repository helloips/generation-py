# https://stepik.org/lesson/265121/step/10?unit=246070

count = 0

is_end = False
while not is_end:
    text = input()
    if text in ('стоп', 'хватит', 'достаточно'):
        is_end = True
    else:
        count += 1

print(count)
