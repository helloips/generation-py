# https://stepik.org/lesson/303084/step/8?unit=284991

SUCCESS_MESSAGE = 'YES'
ERROR_MESSAGE = 'NO'
CORRECT_CHARS = 'АВЕКМНОРСТУХ'


def is_correct_chars(chars):
    for c in chars:
        if c not in CORRECT_CHARS:
            return False
    else:
        return True


def is_correct_car_number(car_number_for_checking):
    car_number_len = len(car_number_for_checking)
    if car_number_len not in (9, 10):
        return False
    elif not (car_number_for_checking[0]).isalpha() or not is_correct_chars(car_number_for_checking[0]):
        return False
    elif not (car_number_for_checking[1:4]).isdigit():
        return False
    elif not (car_number_for_checking[4:6]).isalpha() or not is_correct_chars(car_number_for_checking[4:6]):
        return False
    elif car_number_for_checking[6] != '_':
        return False
    elif car_number_len == 9 and not (car_number_for_checking[7:9]).isdigit():
        return False
    elif car_number_len == 10 and not (car_number_for_checking[7:10]).isdigit():
        return False
    else:
        return True


car_number = input()
print(SUCCESS_MESSAGE if is_correct_car_number(car_number) else ERROR_MESSAGE)
