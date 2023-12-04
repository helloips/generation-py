# https://stepik.org/lesson/303083/step/11?unit=284990

text = input()
count = 0

for i in text:
    if i in "0,1,2,3,4,5,6,7,8,9":
        count += 1

print(count)
