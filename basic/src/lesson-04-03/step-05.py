# https://stepik.org/lesson/265082/step/5?unit=246030

n_1, n_2, n_3 = int(input()), int(input()), int(input())

if n_2 <= n_1 <= n_3 or n_2 >= n_1 >= n_3:
    print(n_1)
elif n_1 <= n_2 <= n_3 or n_1 >= n_2 >= n_3:
    print(n_2)
else:
    print(n_3)
