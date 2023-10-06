# https://stepik.org/lesson/265121/step/8?unit=246070

is_end = False
while not is_end:
    text = input()
    if text == 'КОНЕЦ':
        is_end = True
    else:
        print(text)
