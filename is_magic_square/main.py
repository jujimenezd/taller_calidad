def decode(a: list[int], b: list[str], n: int) -> str:
    """
    Decodifica un mensaje usando un arreglo de índices. Precondición:
    len(a) == len(b) == n, y a contiene una permutación de los enteros 0…n-1.
    Si no se cumple, lanza ValueError.

    Parámetros:
    a – lista de enteros de longitud n.
    b – lista de caracteres de longitud n.
    n – tamaño de los arreglos.

    Retorna:
    Cadena de longitud n formada por los caracteres de b reordenados según los números de a

    Excepciones:
    ValueError("Longitudes inválidas") si len(a) != n o len(b) != n.
    ValueError("a no es permutación de 0…n-1")
        si a no contiene exactamente los números 0,1,…,n-1.
    """
    if len(a) != n or len(b) != n:
        raise ValueError("Longitudes inválidas")

    # Verificar que 'a' es permutación de 0…n-1
    if sorted(a) != list(range(n)):
        raise ValueError("a no es permutación de 0…n-1")

    # Reconstruir el mensaje: en la posición i del resultado va b[a[i]]
    return "".join(b[a[i]] for i in range(n))


# Ejemplo de uso:
if __name__ == "__main__":
    mensaje = decode([2, 0, 1, 6, 4, 3, 5], ["c", "s", "e", "o", "e", "r", "t"], 7)
    print(mensaje)  # imprime: secreto
