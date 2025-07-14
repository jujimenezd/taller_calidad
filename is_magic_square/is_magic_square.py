import numpy as np


def is_magic_square(matrix: list[list[int]]) -> bool:
    if not matrix:
        raise ValueError("La matriz esta vacia")

    matrix = np.array(matrix)
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("La matriz no es cuadrada")

    magic_constant = sum(matrix[0, :])
    rows_and_columns_equal = True
    diagonal_and_inverse_diagonal_equal = True

    for i in range(matrix.shape[0]):
        if sum(matrix[i, :]) != magic_constant or sum(matrix[:, i]) != magic_constant:
            rows_and_columns_equal = False

    sum_diagonal = np.trace(matrix)
    sum_inverse_diagonal = np.fliplr(matrix).diagonal().sum()

    # si la suma de la diagonal es diferente a la constante o la suma de la diagonal inversa es diferente a la constante
    if sum_diagonal != magic_constant or sum_inverse_diagonal != magic_constant:
        diagonal_and_inverse_diagonal_equal = False

    # si las filas y columnas son iguales y la diagonal y la diagonal inversa son iguales a la constante
    if rows_and_columns_equal and diagonal_and_inverse_diagonal_equal:
        return True
    else:
        return False

    """
    Descomentar estas lineas para ver en detalle como se obtienen las filas, columnas, diagonal y la diagonal inversa
    """
    # matrix = np.array(matrix)
    # print(matrix)
    # print()

    # for i in range(matrix.shape[0]):
    #     print("row:", matrix[i, :], "sum:", sum(matrix[i, :]))
    #     print("col:", matrix[:, i], "sum:", sum(matrix[:, i]))
    #     print()
    # print()
    # print("diagonal:", matrix.diagonal(), "sum diagonal:", np.trace(matrix))
    # print(
    #     "inverse diagonal:",
    #     np.fliplr(matrix).diagonal(),
    #     "sum inverse:",
    #     np.fliplr(matrix).diagonal().sum(),
    # )


matrix = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

result = is_magic_square(matrix)

print(result)
