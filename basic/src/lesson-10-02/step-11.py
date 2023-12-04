# https://stepik.org/lesson/313233/step/11?unit=295750

text = input()

h_first_position = text.find("h")
h_last_position = text.rfind("h")
result = text[:h_first_position + 1] + text[h_last_position - 1:h_first_position:-1] + text[h_last_position:]

print(result)
