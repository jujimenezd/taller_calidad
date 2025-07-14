def merge_sorted_arrays(list_1: list[int], list_2: list[int]) -> list[int]:
    if len(list_1) <= 0 or len(list_2) <= 0:
        raise ValueError("Una de las listas esta vacia")

    list_1.sort()
    list_2.sort()
    list_combinated = list_1 + list_2
    list_combinated.sort()

    return list_combinated


list_1 = [1, 2, 2]
list_2 = [1]
result = merge_sorted_arrays(list_1, list_2)

print(result)
