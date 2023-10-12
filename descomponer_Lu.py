from mezclas import mezclar_filas
import numpy as np

arrayTrabajar = [
    [0, 1, -3],
    [0, 3, 2],
    [3, 1, -3]
]

def verificarDescomponerLu(arrayTrabajar):
    CAMBIOFILAS = {
        0: "no se intercambiaron las filas ",
        1: "se intercambiaron la fila 2 y 3",
        2: "se intercambiaron la fila 1 y 2",
        3: "se intercambio la fila 1 por la 2, la 2 por la 3 y la 3 por la 1",
        4: "se intercambio la fila 1 por la 3, la 2 por la 1 y la 3 por la 2",
        5: "se intercambio la fila 1 y 3",
    }
    array = mezclar_filas(arrayTrabajar)
    i = 0
    lon = len(array)-1
    data = descomponerLu(array[i])

    while not data and i < lon:
        i += 1
        data = descomponerLu(array[i])

    if data:
        L = data["L"]
        U = data["U"]

        return {"L": L, "U": U}
    else:
        return False
 


def descomponerLu(arrayTrabajar):

    fila1, fila2, fila3 = arrayTrabajar
    a11, a12, a13 = fila1
    a21, a22, a23 = fila2
    a31, a32, a33 = fila3
    try:

        u11 = a11
        u12 = a12
        u13 = a13
        l21 = a21/u11
        l31 = a31/u11
        u22 = a22-(l21*u12)
        u23 = a23 - (l21*u13)

        l32 = (a32-(l31*u12))/u22
        u33 = (a33) - (l31*u13) - (l32*u23)

    except ZeroDivisionError:
        return False

    except:
        return False
    else:
        return {
            "L": [
                [1, 0, 0],
                [l21, 1, 0],
                [l31, l32, 1],
            ],
            "U": [
                [u11, u12, u13],
                [0, u22, u23],
                [0, 0, u33],
            ]
        }

def resolverSistema(terminos, cohefientes):
    data = verificarDescomponerLu(terminos)
    # L,U = data["L"], data["U"]

    print(data)

