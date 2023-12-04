# https://stepik.org/lesson/303083/step/13?unit=284990

text = input()
symbol = ""
max_numbers_of_symbol = 0

for i in text:
    numbers_of_current_symbol = text.count(i)
    if numbers_of_current_symbol >= max_numbers_of_symbol:
        symbol = i
        max_numbers_of_symbol = numbers_of_current_symbol

print(symbol)
