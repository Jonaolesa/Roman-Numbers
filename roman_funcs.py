valors = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}

def to_roman(n):

    order, d = calc_d_order(n)

    if d <= 3:
        result = d * valors[order]
    elif d == 4:
        result = valors[order] + valors[5*order]
    elif d < 9:
        result = valors[5*order] + (d - 5) * valors[order]
    elif d == 9:
        result = valors[order] + valors[10*order]

    return result


def calc_d_order(n):
    order = 10**(len(str(n))-1)
    d = n//order
    return order, d





def dividir_en_digitos(n:int):
    """"
    TODO : evitar que entren mayores de 3999. lanzar valueError.
    """
    
    
    
    
    cad = f"{n:04d}"
    millares = centenas = decenas = unidades = 0

    millares = int(cad[0]) * 1000
    centenas = int(cad[1]) * 100
    decenas = int(cad[2]) * 10
    unidades = int(cad[3]) * 1

    return [millares,centenas,decenas,unidades]

def digit_to_roman(lista):
    result = ""
    for item in lista:
        result += to_roman(item)
    return result

    
def arabigo_a_romano(n:int):
    lista = dividir_en_digitos(n)
    return digit_to_roman(lista)