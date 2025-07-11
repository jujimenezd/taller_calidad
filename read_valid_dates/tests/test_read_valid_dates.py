import pytest

from read_valid_dates.read_valid_dates import format_date, read_txt


# test para la funcion format_date
@pytest.mark.parametrize(
    "date, expected",
    [
        ("10/01/2025", "2025-01-10"),
        ("01/10/2025", "2025-10-01"),
        ("10/01/2025", "2025-01-10"),
    ],
)
def test_format_date_params(date, expected):
    assert format_date(date) == expected


# test para manejo de errores en format_date
@pytest.mark.parametrize(
    "date",
    [
        "",
        "10/01/2025/10/01/2025",
        "30/022025",
        "",
        "texto_plano_equizde",
        "54/10/0",
        "22/1/0000",
        "5/5/2020",
    ],
)
def test_format_date_value_error_params(date):
    assert format_date(date) is None


"test que demuestra que las opciones alternativas no funcionan correctamente"
# def test_format_date_value_error_params(date):
#     with pytest.raises(ValueError):
#         format_date(date)


def test_read_txt_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_txt("jasajsjw.txt")
