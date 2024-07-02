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
    
    if n <= 3:
        result = n * valors[1]
    elif n == 4:
        result = valors[1] + valors[5]
    elif n <9:
        result = valors[5] + (n-5) * valors[1]
    elif n == 9:
        result = valors[1] + valors[10]
    elif n<= 30:
        result = n//10 * valors[10]
    elif n == 40:
        result = valors[10] + valors[50]
    elif n < 90:
        result = valors[50] + (n//10 - 5) * valors[10]
    elif n == 90:
        result = valors[10] + valors[100]
    elif n <=300:
        result = n // 100 * valors[100]
    elif n == 400:
        result = valors[100] + valors[500]
    elif n <900:
        result = valors[500] + (n-500) //100 * valors[100]
    elif n == 900:
        result = valors[100] + valors[1000]
    elif n <= 3000:
        result = n // 1000 * valors[1000]
    
    else:
        result = valors[n]


    return result





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