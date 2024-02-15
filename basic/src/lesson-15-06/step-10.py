# https://stepik.org/lesson/349851/step/10?unit=333706

def convert_to_decimal(number, from_system):
    number = list(number)[::-1]
    total = 0
    for i in range(len(number)):
        if not number[i].isdigit():
            number[i] = ord(number[i]) - 55
        total += int(number[i]) * from_system ** i
    return total


def convert_from_decimal(number, to_system):
    scaled_number = ''
    if to_system <= 10:
        if number < to_system:
            return number
        while number >= to_system:
            scaled_number += str(number % to_system)
            number //= to_system
        scaled_number += str(number)
        return scaled_number[::-1]
    else:
        if to_system > number > 9:
            return chr(55 + number)
        elif number < to_system and number <= 9:
            return number
        else:
            while number >= to_system:
                remain = number % to_system
                if remain > 9:
                    scaled_number += chr(remain + 55)
                else:
                    scaled_number += str(remain)
                number //= to_system
            scaled_number += str(number)
        return scaled_number[::-1]


in_number = int(input())
print(convert_from_decimal(in_number, 2))
print(convert_from_decimal(in_number, 8))
print(convert_from_decimal(in_number, 16))
