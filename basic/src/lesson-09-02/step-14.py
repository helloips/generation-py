# https://stepik.org/lesson/302627/step/14?unit=284520

text = input()

text_len = len(text)
threshold = text_len // 2 + text_len % 2

first_part = text[:threshold]
second_part = text[threshold:]
result = second_part + first_part

print(result)
