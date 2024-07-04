#TEST

Crear una función que pase de número arábigo a romano (menor de 4000)
to_roman(n: int) -> str
Prueba de unidades simples
Prueba de números que suman de mayor a menor
Después de la investigación hemos decidido que hay un buen algoritmo.

Dividir el número (siempre menor de 4000) en millares, centenas, decenas y unidades. Ponerse en una lista
Procesar cada elemento de la lista transformándolo en romano. Tendre que retocar el algoritmo que ya tengo
Concatenar de mayor a menor los símbolos romanos obtenidos

#NUMEROS MAYORES DE 3999
1. Dividir el numero en miles (grupos de tres digitios de derecha a izquierda. Si el ultimo es menor de 4 se añade ese digito al grupo de tres anterior, quedando como grupo de 4 menor de 4000)

2. Los numeros los vamos a poner en una lista ordenada de derecha a izquiuerda

3. Iterar sobre la lista para conseguir el numero romano y añadirle * por posicion en la lista

4. Concatenar en orden de menos a mas asteriscos cada uno de los romanos


