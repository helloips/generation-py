# https://stepik.org/lesson/416753/step/10?unit=406261

def calculate_next_pascal_line(previous_line):
    if len(previous_line) == 0:
        return [1]

    pascal_line = list()

    pascal_line.append(1)

    if len(previous_line) > 1:
        for index in range(len(previous_line) - 1):
            pascal_line.append(previous_line[index] + previous_line[index + 1])

    pascal_line.append(1)
    return pascal_line


pascal_length = int(input())
current_pascal_line = []
for i in range(pascal_length + 1):
    current_pascal_line = calculate_next_pascal_line(current_pascal_line)

print(current_pascal_line)
