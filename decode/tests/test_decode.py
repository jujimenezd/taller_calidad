import pytest

from decode.decode import decode


@pytest.mark.parametrize(
    "a, b, n, expected",
    [
        ([1, 2, 0, 5, 4, 6, 3], ["c", "s", "e", "o", "e", "r", "t"], 7, "secreto"),
        ([0, 1, 2, 3, 4], ["h", "o", "l", "a", "!"], 5, "hola!"),
        ([3, 2, 1, 0], ["a", "m", "o", "r"], 4, "roma"),
        ([1, 0, 2, 3, 4], ["u", "m", "n", "d", "o"], 5, "mundo"),
        ([1, 0, 3, 2], ["i", "v", "a", "d"], 4, "vida"),
        ([4, 3, 2, 1, 0], ["o", "d", "n", "u", "m"], 5, "mundo"),
        (
            [1, 3, 5, 2, 7, 0, 6, 4],
            ["a", "p", "g", "r", "a", "o", "m", "r"],
            8,
            "programa",
        ),
        ([0, 2, 1, 3], ["c", "d", "o", "e"], 4, "code"),
    ],
)
def test_decode_params(a, b, n, expected):
    assert decode(a, b, n) == expected


def test_decode_empty_list():
    with pytest.raises(ValueError, match="Una de las listas esta vacia"):
        decode([], [], 0)
        decode([1, 2, 3], [], 3)
        decode([], [1, 2, 3], 3)


def test_decode_invalid_permutation():
    with pytest.raises(ValueError, match="a no es una permutación de 0…n-1"):
        decode([1, 2, 3, 4], ["a", "b", "c", "d"], 4)
        decode([1, 2, 2, 1], ["a", "b", "c", "d"], 4)
        decode([1, 2, 3, 4, 5, 8, 8], ["a", "b", "c", "d", "e", "f", "g"], 7)
        decode([1, 1, 1, 1], ["a", "b", "c", "d"], 4)


def test_decode_invalid_length():
    with pytest.raises(ValueError, match="Una de las listas es incompatible"):
        decode([0, 2, 5, 7], ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"], 10)
        decode(
            [1, 5, 2, 3, 0, 9, 8, 2],
            ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
            10,
        )
