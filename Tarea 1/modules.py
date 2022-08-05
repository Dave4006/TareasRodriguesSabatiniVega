
# función de suma devuelve el resultado de Op1+Op2,
# quienes son sus parámetros de entrada
def suma(op1, op2):
    return op1+op2


# función de resta devuelve el resultado de Op1-Op2,
# quienes son sus parámetros de entrada
def resta(op1, op2):
    return op1-op2


# función de división devuelve el resulto de Op1/Op2,
# quienes son sus parámetros de entrada,
# siempre y cuando Op2 != 0, si no devuelve el error E1
def division(op1, op2):
    if op2 != 0:
        return op1/op2
    else:
        return 'E1'

# Se crea una clase llamada Modules para poder llamarla
# e utilizarla como objeto en el código de los testeos;
# contiene las funciones basic_operations y count_char.


class Modules:

    # basic_operations obtiene como parámetros de entrada a Op1, Op2 y OP,
    # los cuales son 1er operando, 2do operando y operación, respectivamente.
    # Esta función se encarga de validar los datos y llamar a las funciones de
    # las operaciones correspondientes a cada valor válido de OP,
    # usando un diccionario para relacionar cada operación con su valor de OP.
    # También si hay un error esta función devuelve el código correspondiente.

    # Códigos de error:
    # E0: uno o varios parámetros de entrada no son enteros.
    # E1: no se puede realizar la división porque Op2 = 0.
    # E2: El valor de OP no es ninguno de los valores válidos.
    def basic_operations(Op1, Op2, OP):
        # Se valida que los parámetros de entrada sean enteros
        if isinstance(Op1, int) & isinstance(Op2, int) & isinstance(OP, int):
            # Si todos son enteros se devuelve el resultado generado
            # por la función llamada por el diccionario, si el valor
            # de OP no está en el diccionario este devuelve E2 como error.
            return {1: suma(Op1, Op2),  # si OP = 1 se llama a suma()
                    2: resta(Op1, Op2),  # si OP = 2 se llama a resta()
                    3: division(Op1, Op2)}.get(OP, 'E2')
            # si OP = 3 se llama a division()
            # y si no es un valor válido se da el error E2.

        # Si uno o varios parámetros de entrada no son enteros
        # se develve el error E0.
        else:
            return 'E0'

    # La función count_char recibe un valor Input como parámetro de entrada,
    # valida si este valor es un string
    # y calcula la cantidad de caracteres que lo conforman.
    # Si Input no es un string devuelve el error E3.

    # Códigos de error:
    # E3: el parámetro de entrada Input no es string.
    def count_char(Input):
        if isinstance(Input, str):  # valida si Input es string.
            return len(Input)  # calcula y devuelve la cantidad de caracteres.
        else:  # si input no es string devuelve un error.
            return 'E3'
