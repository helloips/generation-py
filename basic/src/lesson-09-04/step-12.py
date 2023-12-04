# https://stepik.org/lesson/303083/step/12?unit=284990

text = input()
is_correct_uri = False

if text.endswith(".ru") or text.endswith(".com"):
    is_correct_uri = True

print("YES" if is_correct_uri else "NO")
