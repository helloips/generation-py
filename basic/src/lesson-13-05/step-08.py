# https://stepik.org/lesson/334150/step/8?unit=317559

def is_palindrome(num):
    actual_chars = [i for i in str(num)]
    return actual_chars == actual_chars[::-1]


def is_prime(num):
    return len([i for i in range(1, num + 1) if num % i == 0]) == 2


# объявление функции
def is_valid_password(password):
    parts = [int(i) for i in password.split(':')]
    return len(parts) == 3 and is_palindrome(parts[0]) and is_prime(parts[1]) and parts[2] % 2 == 0


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
