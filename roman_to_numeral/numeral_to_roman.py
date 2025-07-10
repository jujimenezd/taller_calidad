roman_representation = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}


def number_to_roman(number):
    roman_expression = ""

    if number <= 0 or number >= 4000:
        raise ValueError("el numero esta fuera del rango")

    for roman_value, value in roman_representation.items():
        while number >= value:
            roman_expression += roman_value
            number -= value
    return roman_expression
