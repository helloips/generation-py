# https://stepik.org/lesson/294080/step/4?unit=275759

n = int(input())

print('*' * 19)
for _ in range(n - 2):
    print('*', ' ' * 17, '*', sep='')
print('*' * 19)
