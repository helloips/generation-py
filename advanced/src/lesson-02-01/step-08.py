# https://stepik.org/lesson/415553/step/8?unit=405082

AMERICAN_DELIMITER = ','

number_as_string = input()
number_as_string_len = len(number_as_string)
american_number_as_string = ''

if number_as_string_len < 4:
    american_number_as_string = number_as_string
else:
    index = 1
    for char in number_as_string[::-1]:
        if index % 3 == 0 and index < number_as_string_len:
            american_number_as_string += char + AMERICAN_DELIMITER
        else:
            american_number_as_string += char
        index += 1
    american_number_as_string = american_number_as_string[::-1]


print(american_number_as_string)
