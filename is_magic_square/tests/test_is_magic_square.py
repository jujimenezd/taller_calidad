import pytest

from is_magic_square.is_magic_square import is_magic_square


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[2, 7, 6], [9, 5, 1], [4, 3, 8]], True),
        ([[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]], True),
        ([[1, 2], [3, 4]], False),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], True),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], False),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], False),
    ],
)
def test_is_magic_square_params(matrix, expected):
    assert is_magic_square(matrix) == expected


def test_is_magic_square_empty_matrix():
    with pytest.raises(ValueError, match="La matriz esta vacia"):
        is_magic_square([])


def test_is_magic_square_not_square_matrix():
    with pytest.raises(ValueError, match="La matriz no es cuadrada"):
        is_magic_square([[1, 2, 3], [4, 5, 6]])
        is_magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
        is_magic_square([[1, 2, 3]])
