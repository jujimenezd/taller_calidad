from datetime import datetime
import os


def format_date(date: str) -> str:
    valid_date = False

    date = date.strip()
    dates = date.split("/")
    dates.reverse()
    date_formated = "-".join(dates)

    # try que valida si la fecha formateada es valida segun el formato ISO 8601 (YYYY-MM-DD)
    try:
        datetime.fromisoformat(date_formated)
        valid_date = True
    except Exception as e:
        valid_date = False
        print(f"fecha invalida --> {date_formated} || error --> {e}")

    if valid_date:
        return date_formated
    return None

    """
    formas alternativas para validar la fecha, funcionan pero haciendo testing fallan al momento
    de validar el formato correcto de la fecha, por ejemplo: 5/5/2020 por la norma ISO 8601 no es valido, pero la implementacion la toma como valida.
    """
    # date_format = "%d/%m/%Y"
    # try:
    #     date_formated = datetime.datetime.strptime(date, date_format)
    #     date_formated = date_formated.strftime("%Y-%m-%d")
    #     return date_formated
    # except ValueError:
    #     print(f"Formato de fecha incorrecto: {date}")

    # if len(dates) != 3:
    #     raise ValueError(f"Formato de fecha incorrecto: {date}")
    # dates.reverse()
    # date_formated = "-".join(dates)
    # return date_formated


def read_txt(file_path: str) -> list:
    try:
        with open(file_path, "r") as file:
            dates = file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo {file_path} no existe")
    return dates


def read_valid_dates(file_path: str) -> list:
    dates = read_txt(file_path)
    valid_dates = []

    for date in dates:
        date_formated = format_date(date)

        if date_formated is None:
            continue
        valid_dates.append(date_formated)

    valid_dates.sort()
    return valid_dates


# Usar la ruta relativa a la carpeta read_valid_dates
directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(directory, "fechas.txt")

dates = read_valid_dates(file_path)
print(dates)
