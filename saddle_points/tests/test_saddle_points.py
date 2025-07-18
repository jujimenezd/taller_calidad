import pytest

from saddle_points.saddle_points import saddle_points


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[9, 8, 7], [5, 3, 2], [6, 6, 7]], [(1, 0)]),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [(0, 2)]),
        ([[3, 1, 3], [3, 2, 4], [2, 5, 4]], [(0, 2)]),
        ([[4, 5, 4], [3, 5, 5], [1, 5, 4]], [(0, 1), (1, 1), (2, 1)]),
        ([[8, 7, 9], [6, 7, 6], [3, 2, 5]], [(2, 2)]),
        ([[3, 2, 1], [2, 1, 0], [1, 0, -1]], [(2, 0)]),
        ([[2, 2], [2, 2]], [(0, 0), (0, 1), (1, 0), (1, 1)]),
        ([[1]], [(0, 0)]),
        ([[]], []),
        ([[5, 5], [5, 5]], [(0, 0), (0, 1), (1, 0), (1, 1)]),
    ],
)
def test_saddle_points_params(matrix, expected):
    assert saddle_points(matrix) == expected
