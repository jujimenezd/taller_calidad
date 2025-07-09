import pytest

from check_password.check_password import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("12345678", False),
        ("Colombia10866#", True),
        ("@C0l0mb1a10866#", True),
        ("pass$W0rd", True),
        ("abc", False),
        ("0000000", False),
        ("AAAAAAAAAAA", False),
        ("AAAAAAAAAAA", False),
        ("Programacion 1234 $", False),
        ("", False),
        ("Software$_EnginneR", False),
        ("1234abcd'", True),
        ("True", False),
        ("Str0ng&PW!", True),
        ("@@@@@@@@@@@@", False),
        ("Good@Pass", False),
    ],
)
def test_check_password_params(password, expected):
    assert check_password(password) == expected
