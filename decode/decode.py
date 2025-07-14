def decode(a: list[int], b: list[str], n: int) -> str:
    if not a or not b:
        raise ValueError("Una de las listas esta vacia")

    if len(a) != n or len(b) != n:
        raise ValueError("Una de las listas es incompatible")

    # Comprueba que la lista con el mensaje codificado tenga los numeros de 0 a n-1
    if set(a) != set(range(n)):
        raise ValueError("a no es una permutación de 0…n-1")

    message = ""
    # decodifica el mensaje accediendo a cada valor de la lista a y luego accede a la lista b con ese indice
    for i in range(n):
        message += b[a[i]]
    return message


# Ejemplo de uso:
if __name__ == "__main__":
    mensaje = decode([1, 2, 0, 5, 4, 6, 3], ["c", "s", "e", "o", "e", "r", "t"], 7)
    print(mensaje)  # imprime: secreto
