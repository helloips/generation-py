# https://stepik.org/lesson/313439/step/6?unit=295959

delta = int(input())
text = input()

for i in text:
    correct_uni = ord(i) - delta
    if correct_uni < 97:
        correct_uni += 26
    print(chr(correct_uni), end="")
