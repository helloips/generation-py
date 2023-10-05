# https://stepik.org/lesson/265115/step/9?unit=246063

len_1 = len(input())
len_2 = len(input())
len_3 = len(input())

max_len = max(len_1, len_2, len_3)
min_len = min(len_1, len_2, len_3)
middle_len = len_1 + len_2 + len_3 - max_len - min_len

if max_len - middle_len == middle_len - min_len:
    print('YES')
else:
    print('NO')
