import pytest
from add_digits_arrays.add_digits_arrays import add_digits_arrays


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 2, 3], [4, 5, 6], [5, 7, 9]),
        ([0, 0], [0, 0], [0]),
    ],
)
def test_add_digit_arrays_basic(a, b, expected):
    assert add_digits_arrays(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([9, 9], [1], [1, 0, 0]),
        ([1], [9, 9], [1, 0, 0]),
        ([5, 5], [5, 5], [1, 1, 0]),
    ],
)
def test_add_digit_arrays_with_carry(a, b, expected):
    assert add_digits_arrays(a, b) == expected


@pytest.mark.parametrize(
    "a, b",
    [
        ([], []),
        ([1, 2, 3], []),
        ([], [4, 5, 6]),
    ],
)
def test_add_digit_arrays_empty_list_raises(a, b):
    with pytest.raises(ValueError):
        add_digits_arrays(a, b)


@pytest.mark.parametrize(
    "a, b",
    [
        (None, [1, 2, 3]),
        ([1, 2, 3], None),
        ("not a list", [1, 2, 3]),
        ([1, 2, 3], "not a list"),
    ],
)
def test_add_digit_arrays_type_error(a, b):
    with pytest.raises(TypeError):
        add_digits_arrays(a, b)


@pytest.mark.parametrize(
    "a, b",
    [
        ([1, "2", 3], [4, 5, 6]),
        ([1, -1, 3], [4, 5, 6]),
        ([10, 2, 3], [4, 5, 6]),
    ],
)
def test_add_digit_arrays_invalid_digits(a, b):
    with pytest.raises(ValueError):
        add_digits_arrays(a, b)
