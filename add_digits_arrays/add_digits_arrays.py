def add_digits_arrays(list_1: list[int], list_2: list[int]) -> list[int]:
    if not isinstance(list_1, list) or not isinstance(list_2, list):
        raise TypeError("solo se permiten listas de digitos")

    if not list_1 or not list_2:
        raise ValueError("una de las listas esta vacia o no son listas")

    list_combinated = list_1 + list_2

    for i in list_combinated:
        if not isinstance(i, int):
            raise ValueError("solo se permiten numeros enteros")
        if i < 0 or i > 9:
            raise ValueError("solo pueden ser numeros del 0 al 9")

    # se realiza un map en cada lista, le aplicamos la funcion str para convertir
    # cada elemento de la lista y luego concatenamos cada digito con un join
    # y finalmente transformamos el str resultante a int.
    total = int("".join(map(str, list_1))) + int("".join(map(str, list_2)))

    return [int(digit) for digit in str(total)]


result = add_digits_arrays([1, 2, 3], [9, 9])

print(result)
