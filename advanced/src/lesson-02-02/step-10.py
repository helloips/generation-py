# https://stepik.org/lesson/415554/step/10?unit=405083

AI_NAME = 'anton'

n = int(input())
names = list()
result = list()

for _ in range(n):
    names.append(input())

for name_index in range(len(names)):
    verifiable_name = names[name_index]
    name_indexes = [-1] * len(AI_NAME)

    start_index = 0
    for current_char_index in range(len(AI_NAME)):
        current_char = AI_NAME[current_char_index]
        verifiable_name = (verifiable_name[start_index:])
        index = verifiable_name.find(current_char)
        if index != -1:
            start_index = index
            name_indexes[current_char_index] = index

    is_ai = True
    for i in name_indexes:
        if i == -1:
            is_ai = False
            break

    if is_ai:
        result.append(name_index + 1)

print(*result)
