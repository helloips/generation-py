# https://stepik.org/lesson/416753/step/14?unit=406261

def get_sub_lists(all_symbols):
    all_sub_lists = list()
    all_sub_lists.append([])

    for size in range(1, len(all_symbols) + 1):
        for start in range(len(all_symbols)):
            current_sub_list = all_symbols[start:start+size]
            if len(current_sub_list) == size:
                all_sub_lists.append(all_symbols[start:start+size])

    return all_sub_lists


print(get_sub_lists(input().split()))
