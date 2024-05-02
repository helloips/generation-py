# https://stepik.org/lesson/415553/step/7?unit=405082

number_as_string = input()
reversed_number_as_string = ''

if len(number_as_string) == 5:
    reversed_number_as_string = number_as_string[::-1]
elif len(number_as_string) == 6:
    reversed_number_as_string = number_as_string[0] + (number_as_string[1::])[::-1]

print(int(reversed_number_as_string))
