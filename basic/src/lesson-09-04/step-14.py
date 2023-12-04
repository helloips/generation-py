# https://stepik.org/lesson/303083/step/14?unit=284990

text = input()
first_position = -1
last_position = -1

first_position = text.find("f")
last_position = text.rfind("f")

if first_position == -1 and last_position == -1:
    print("NO")
elif first_position == last_position:
    print(first_position)
else:
    print(first_position, last_position)
