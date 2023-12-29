# https://stepik.org/lesson/334150/step/4?unit=317559

def is_prime(num):
    return len([i for i in range(1, num + 1) if num % i == 0]) == 2


# объявление функции
def get_next_prime(num):
    digit = num + 1
    while True:
        if is_prime(digit):
            return digit
        digit += 1


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
