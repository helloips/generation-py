# https://stepik.org/lesson/265121/step/14?unit=246070

total_price = int(input())
total_number_of_coins = 0

for coin_denomination in (25, 10, 5, 1):
    number_of_coins = total_price // coin_denomination
    total_price -= number_of_coins * coin_denomination
    total_number_of_coins += number_of_coins

print(total_number_of_coins)
