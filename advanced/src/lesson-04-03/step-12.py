# https://stepik.org/lesson/416753/step/12?unit=406261

symbols = input().split()
symbols.append('*')
symbol_groups = list()

previous_symbol = symbols[0]
current_symbol_group = [previous_symbol]

for current_symbol in symbols[1:]:
    if current_symbol == previous_symbol:
        current_symbol_group.append(current_symbol)
    else:
        symbol_groups.append(current_symbol_group)
        current_symbol_group = [current_symbol]
    previous_symbol = current_symbol

print(symbol_groups)
