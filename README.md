# Taller de Calidad de Software

Este repositorio contiene una colección de ejercicios prácticos para testear la calidad del código.

## Estructura del Repositorio

Cada carpeta contiene un problema específico con su implementación y pruebas unitarias:

- **add_digits_arrays**: Suma de arrays de dígitos
- **check_password**: Validación de contraseñas
- **decode**: Decodificación de mensajes
- **is_magic_square**: Verificación de cuadrados mágicos
- **merge_sorted_arrays**: Combinación de arrays ordenados
- **perfect_numbers**: Cálculo de números perfectos
- **read_valid_dates**: Lectura y validación de fechas
- **roman_to_numeral**: Conversión entre números romanos y arábigos
- **saddle_points**: Identificación de puntos de silla en matrices
- **validate_username**: Validación de nombres de usuario

## Requisitos

- Python 3.8 o superior

## Configuraciones iniciales

- Crear un entorno virtual

```bash
python -m venv venv
```

- Activar el entorno virtual

- En Bash

```bash
source venv/bin/activate
```

- En PowerShell

```bash
cd venv
.\Scripts\activate
```

- Instalar las dependencias

```bash
pip install -r requirements.txt
```

## Ejecución de Pruebas

Cada ejercicio incluye su propio conjunto de pruebas unitarias en la carpeta `tests/`.

Para ejecutar las pruebas de un ejercicio específico:

```bash
 cd nombre_del_ejercicio
 pytest -v
```

Para ejecutar todas las pruebas del repositorio:

```bash
pytest -v
```

## Directrices de cada problema

Los ejercicios siguen estas directrices:

1. Cada problema está contenido en su propia carpeta
2. Cada implementación incluye validaciones de entrada apropiadas
3. Las pruebas unitarias verifican tanto casos normales como casos atípicos
4. Se utilizan excepciones para manejar errores de manera adecuada
