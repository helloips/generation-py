# https://stepik.org/lesson/313233/step/10?unit=295750

text = input()

f_count = text.count("f")

if f_count == 0:
    print(-2)
elif f_count == 1:
    print(-1)
else:
    f_first_position = text.find("f")
    print(text.find("f", f_first_position + 1))
