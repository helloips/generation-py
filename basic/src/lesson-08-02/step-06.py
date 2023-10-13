# https://stepik.org/lesson/294080/step/6?unit=275759

n = int(input())

last_digit = n % 10

three_digit_count = 0
last_digit_count = 0
even_digit_count = 0
more_five_digit_sum = 0
more_seven_digit_product = 1
zero_or_five_digit_count = 0

while n > 0:
    digit = n % 10

    if digit == 3:
        three_digit_count += 1
    if digit == last_digit:
        last_digit_count += 1
    if digit % 2 == 0:
        even_digit_count += 1
    if digit > 5:
        more_five_digit_sum += digit
    if digit > 7:
        more_seven_digit_product *= digit
    if digit == 0 or digit == 5:
        zero_or_five_digit_count += 1

    n //= 10

print(three_digit_count)
print(last_digit_count)
print(even_digit_count)
print(more_five_digit_sum)
print(more_seven_digit_product)
print(zero_or_five_digit_count)
