def get_divisors(number: int):
    divisors = []

    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)

    return divisors


def perfect_numbers(number: int):
    list_perfect_numbers = []

    if number <= 0:
        raise ValueError("el numero debe ser mayor a 0")

    for i in range(1, number + 1):
        divisors = get_divisors(i)
        sum_divisors = sum(divisors)

        if sum_divisors == i:
            list_perfect_numbers.append(i)

    return list_perfect_numbers
