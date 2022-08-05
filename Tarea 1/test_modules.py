# Se importa el objeto Modules desde el archivo modules.py y pyset
from modules import Modules
import pytest

# Datos para las pruebas de funcionamiento de basic_operations
# tienen como estructura (Op1, Op2, OP, expected, id para identificación)
# pytest.param() nos permite especificar un ID.
testdata_basic_operations = [
    pytest.param(1, 2, 1, 3, id="suma"),
    pytest.param(1500, 500, 2, 1000, id="resta"),
    pytest.param(9, 3, 3, 3, id="division")
]

# Datos para las pruebas de error E0 y E2 de basic_operations
# tienen como estructura (Op1, Op2, OP, expected, id para identificación)
testdata_basic_operations_E0 = [
    pytest.param('Op1', 2, 1, 'E0', id="Op1 no es entero"),
    pytest.param(1, 'Op2', 1, 'E0', id="Op2 no es entero"),
    pytest.param(1, 2, 'OP', 'E0', id="OP no es entero"),
    pytest.param(1, 2, 4, 'E2', id="OP no es un valor valido")
]

# Datos para las pruebas de error E1 de basic_operations
# tienen como estructura (Op1, Op2, OP, expected, id para identificación)
testdata_basic_operations_E1 = [
    pytest.param(9, 0, 3, 'E1', id="division 9/0"),
    pytest.param(40, 0, 3, 'E1', id="division 40/0"),
    pytest.param(500, 0, 3, 'E1', id="division 500/0")
]

# Datos para las pruebas de funcionamiento de count_char
# tienen como estructura (Input, expected, id para identificación)
testdata_count_char = [
    pytest.param("siete 7", 7, id="1ra prueba conteo"),
    pytest.param("cinco", 5, id="2nda prueba conteo"),
    pytest.param("uno", 3, id="3ra prueba conteo")
]

# Datos para las pruebas de error E3 de count_char
# tienen como estructura (Input, expected, id para identificación)
testdata_count_char_E3 = [
    pytest.param(1.45, 'E3', id="1ra prueba error E3"),
    pytest.param(12, 'E3', id="2nda prueba error E3"),
    pytest.param(0.005, 'E3', id="3ra prueba error E3")
]


# Parametrización de las pruebas de funcionamiento de basic_operations.
# Los parámetros de entrada son los requeridos
# por basic_operations (Op1, Op2 y OP) y
# del parámetro expected, este es el resultado que esperamos recibir.
# Esta también recibe los datos para el testeo.

# Se lleva a cabo el testeo con los parámetros
# anteriormente descritos y se genera el assert
# esperando recibir la respuesta esperada.
@pytest.mark.parametrize("op1, op2, op, expected", testdata_basic_operations)
# creación del test
def test_basic_operations_working(op1, op2, op, expected):
    # inicia tests con un assert
    assert Modules.basic_operations(op1, op2, op) == expected


# Parametrización de las pruebas de error E0 y E2 de basic_operations.
# Se tienen los mismos parámetros y funcionamientos que anteriormente.
@pytest.mark.parametrize("op1, op2, op, expected",
                         testdata_basic_operations_E0)
# creación del test
def test_basic_operations_errors(op1, op2, op, expected):
    # inicia tests con un assert
    assert Modules.basic_operations(op1, op2, op) == expected


# Parametrización de las pruebas de error E1 de basic_operations.
# Se tienen los mismos parámetros y funcionamientos que anteriormente.
@pytest.mark.parametrize("op1, op2, op, expected",
                         testdata_basic_operations_E1)
# creación del test
def test_zero_div(op1, op2, op, expected):
    # inicia tests con un assert
    assert Modules.basic_operations(op1, op2, op) == expected


# Parametrización de las pruebas de funcionamiento de count_char.
# Se tienen los parámetros requeridos por count_char (Input) y el expected.
# Funciona igual que las parametrizaciones anteriores.
@pytest.mark.parametrize("input, expected", testdata_count_char)
# creación del test
def test_count_char_working(input, expected):
    # inicia tests con un assert
    assert Modules.count_char(input) == expected


# Parametrización de las pruebas de error E3 de count_char.
# Se tienen los mismos parámetros y funcionamientos que anteriormente.
@pytest.mark.parametrize("input, expected", testdata_count_char_E3)
# creación del test
def test_count_char_error(input, expected):
    # inicia tests con un assert
    assert Modules.count_char(input) == expected
