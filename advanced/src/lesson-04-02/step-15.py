# https://stepik.org/lesson/416752/step/15?unit=406260

list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
list1 = list(list(reversed(i)) for i in list1)

print(list1)
