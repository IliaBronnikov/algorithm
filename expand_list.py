# Необходимо раскрыть список
# [1, [2, 4, 2, [1]]] - > [1, 2, 4, 2, 1]

# Решение № 1
def expand_list(lst: list) -> list:
    current_list = []

    for elem in lst:
        if isinstance(elem, list):
            current_list.extend(expand_list(elem))
        else:
            current_list.append(elem)
        
    return current_list
