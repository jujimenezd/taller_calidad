import pytest

from merge_sorted_arrays.merge_sorted_arrays import merge_sorted_arrays


@pytest.mark.parametrize(
    "list_1, list_2, expected",
    [
        ([1, 3, 5, 7], [2, 4, 6, 8], [1, 2, 3, 4, 5, 6, 7, 8]),
        ([9, 1, 8, 3], [7, 2, 6, 4], [1, 2, 3, 4, 6, 7, 8, 9]),
        ([5, 5, 5], [1, 1, 1], [1, 1, 1, 5, 5, 5]),
        ([-3, 0, -1], [10, 5, 2], [-3, -1, 0, 2, 5, 10]),
        ([100], [200], [100, 200]),
        ([4, 2, 8], [4, 2, 8], [2, 2, 4, 4, 8, 8]),
        ([9, 9, 8, 8], [7, 7, 6, 6], [6, 6, 7, 7, 8, 8, 9, 9]),
        ([-10, -5, 0, 5, 10], [-8, -4, 0, 4, 8], [-10, -8, -5, -4, 0, 0, 4, 5, 8, 10]),
    ],
)
def test_merge_sorted_arrays_params(list_1, list_2, expected):
    assert merge_sorted_arrays(list_1, list_2) == expected


def test_merge_sorted_arrays_empty_list():
    with pytest.raises(ValueError, match="Una de las listas esta vacia"):
        merge_sorted_arrays([], [])
        merge_sorted_arrays([1, 2, 3], [])
        merge_sorted_arrays([], [1, 2, 3])
