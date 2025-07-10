import pytest
from perfect_numbers.perfect_numbers import perfect_numbers


@pytest.mark.parametrize(
    "number, expected",
    [
        (6, [6]),
        (28, [6, 28]),
        (496, [6, 28, 496]),
        (8128, [6, 28, 496, 8128]),
    ],
)
def test_perfect_numbers_params(number, expected):
    assert perfect_numbers(number) == expected


def test_perfect_numbers_params_value_error():
    with pytest.raises(ValueError):
        perfect_numbers(0)
        perfect_numbers(-1)
