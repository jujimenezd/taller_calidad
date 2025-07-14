import numpy as np


def saddle_points(matrix: list[list[int]]) -> list[tuple[int, int]]:
    if not matrix:
        return []

    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) > 1:
        raise ValueError("irregular matrix")

    matrix = np.array(matrix)

    rows = matrix.shape[0]
    columns = matrix.shape[1]
    saddle_points = []

    for i in range(rows):
        for j in range(columns):
            """
            # matrix[i, j] -> obtenemos el valor de cada elemento de la matriz       (0,0) (0,1) (0,2)
            # matrix[i, :] -> por cada fila obtenemos el valor de todas las columnas (0,0) (0,1) (0,2)
            # matrix[:, j] -> por cada columna obtenemos el valor de todas las fila  (0,0) (1,0) (2,0)
            # max(matrix[i, :]) -> maximo de cada fila
            # min(matrix[:, j]) -> minimo de cada columna
            """
            if matrix[i, j] == max(matrix[i, :]) and matrix[i, j] == min(matrix[:, j]):
                saddle_points.append((i, j))

            """
            descomentar estas lineas para ver en mas detalle todo el proceso
            """
            # print(matrix[i, :])
            # print(matrix[:, j].reshape(-1, 1))  # Mostrar como vector la columna j

            # print(
            #     f"(posicion: {i}, {j}) -> valor: {matrix[i, j]} -> máximo de la fila: {max(matrix[i, :])} -> mínimo de la columna: {min(matrix[:, j])}"
            # )
            # print()

    return saddle_points


matrix = [
    [9, 8, 7],
    [5, 3, 2],
    [6, 6, 7],
]

print(saddle_points(matrix))
