# https://stepik.org/lesson/326725/step/6?unit=310010

palindromes = [i for i in range(100, 1000) if str(i) == str(i)[::-1]]

print(palindromes)
