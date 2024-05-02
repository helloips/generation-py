# https://stepik.org/lesson/303084/step/6?unit=284991

SUCCESS_MESSAGE = 'Correct'
ERROR_MESSAGE = 'Incorrect'


def is_correct_nickname(nickname_for_checking):
    nickname_len = len(nickname_for_checking)
    if nickname_len < 5 or nickname_len > 15:
        return False
    elif nickname_for_checking[0] != '@':
        return False

    for char in nickname_for_checking[1:]:
        if not char.isalpha() and not char.isdigit():
            return False
        elif char.isalpha() and char.isupper():
            return False

    return True


nickname = input()
print(SUCCESS_MESSAGE if is_correct_nickname(nickname) else ERROR_MESSAGE)
