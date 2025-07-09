import pytest
from validate_username.validate_username import is_valid_username


@pytest.mark.parametrize(
    "username, expected",
    [
        ("juanes34", True),
        ("3uanes34", False),
        ("", False),
        ("jujimenezd_23", False),
        ("000000000", False),
        ("juanes34", True),
        ("1", False),
        ("$$#jujimenezd", False),
        ("abc", False),
        ("}{}43juan", False),
    ],
)
def test_validate_username_params(username, expected):
    assert is_valid_username(username) == expected


# def test_validate_username():
#     assert is_valid_username("juanes34") == True
#     assert is_valid_username("3juan34") == False
#     assert is_valid_username("") == False
#     assert is_valid_username("jujimenezd_23") == False
#     assert is_valid_username("jujimenezd_") == True
#     assert is_valid_username("000000000") == False
#     assert is_valid_username("1") == False
#     assert is_valid_username("A") == False
#     assert is_valid_username("$$#jujimenezd") == False
#     assert is_valid_username("DUNKELHEIT") == True
#     assert is_valid_username("Tragamilk") == True
