import pytest

from roman_to_numeral.numeral_to_roman import number_to_roman


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, "I"),
        (4, "IV"),
        (9, "IX"),
        (14, "XIV"),
        (19, "XIX"),
        (23, "XXIII"),
        (42, "XLII"),
        (99, "XCIX"),
        (100, "C"),
        (246, "CCXLVI"),
        (321, "CCCXXI"),
        (499, "CDXCIX"),
        (500, "D"),
        (678, "DCLXXVIII"),
        (777, "DCCLXXVII"),
        (888, "DCCCLXXXVIII"),
        (999, "CMXCIX"),
        (1000, "M"),
        (1234, "MCCXXXIV"),
        (1492, "MCDXCII"),
        (1776, "MDCCLXXVI"),
        (1918, "MCMXVIII"),
        (2023, "MMXXIII"),
        (2222, "MMCCXXII"),
        (2500, "MMD"),
        (2999, "MMCMXCIX"),
        (3000, "MMM"),
        (3333, "MMMCCCXXXIII"),
        (3752, "MMMDCCLII"),
        (3999, "MMMCMXCIX"),
    ],
)
def test_roman_params(number, expected):
    assert number_to_roman(number) == expected


@pytest.mark.parametrize(
    "number",
    [
        0,
        4000,
        -1,
    ],
)
def test_roman_params_value_error_params(number):
    with pytest.raises(ValueError):
        number_to_roman(number)
