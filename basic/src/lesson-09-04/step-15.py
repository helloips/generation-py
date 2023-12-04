# https://stepik.org/lesson/303083/step/15?unit=284990

text = input()

first_position = text.find("h")
last_position = text.rfind("h")
result = text[:first_position] + text[last_position + 1:]

print(result)
