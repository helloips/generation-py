# https://stepik.org/lesson/324754/step/8?unit=307930

n = int(input().replace('#', ''))
lines = list()

for i in range(n):
    line = input()
    comment_index = line.find('#')
    if comment_index > -1:
        line = line[:comment_index]
    lines.append(line.rstrip())

print(*lines, sep="\n")
