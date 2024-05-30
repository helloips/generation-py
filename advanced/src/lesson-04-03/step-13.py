# https://stepik.org/lesson/416753/step/13?unit=406261

def chunked(all_symbols, group_size):
    all_symbol_groups = list()
    current_symbol_group = list()

    for symbol in all_symbols:
        if len(current_symbol_group) < group_size:
            current_symbol_group.append(symbol)
        else:
            all_symbol_groups.append(current_symbol_group.copy())
            current_symbol_group = [symbol]
    else:
        if len(current_symbol_group) > 0:
            all_symbol_groups.append(current_symbol_group.copy())

    return all_symbol_groups


print(chunked(input().split(), int(input())))
