#Ejercicio 1
cantidad_de_digitos = 0
def digitos(numero_de_tarjeta: str) -> int:
    return len(numero_de_tarjeta)

#Ejercicio 2
def obtener_prefijo(numero_de_tarjeta: str,tamaño_prefijo: int) -> int:
    return int(numero_de_tarjeta[:tamaño_prefijo])

    return

#Ejercicio 3
def tipo_tarjeta(numero_de_tarjeta: str) -> str:
    x = obtener_prefijo(numero_de_tarjeta,2)
    d = digitos(numero_de_tarjeta)
    y = obtener_prefijo(numero_de_tarjeta,1)
    condicion_master =  (x >= 51 and x <= 55) and d == 16   #Pueden borrar el False y completar
    condicion_visa   =  y == 4 and (d == 13 or d == 16)          #Pueden borrar el False y completar
    condicion_amex   = (x == 34 or x == 37) and d == 15       #Pueden borrar el False y completar
   
    if condicion_master:
        return 'Mastercard'
   
    elif condicion_visa:
        return 'Visa'
  
    elif condicion_amex:
        return 'American Express'
    else:
        return 'Invalid'


#Ejercicio 4
def digitos_impares(numero_de_tarjeta : str) -> list[int]:
    numero = int(numero_de_tarjeta)
    reversed_numero_string = str(numero)[::-1]
    if type(numero) == int:
        reversed_numero = int(reversed_numero_string)
    numero_str = str(reversed_numero)

    list=[]

    for i in range(0, len(numero_str), 2):
        print(numero_str[i])
        list.append(int(numero_str[i]))
    
    return(list)

#Ejercicio 5
def digitos_pares(numero_de_tarjeta: str) -> list[int]:
    numero = int(numero_de_tarjeta)
    reversed_numero_string = str(numero)[::-1]
    if type(numero) == int:
        reversed_numero = int(reversed_numero_string)
    numero_str = str(reversed_numero)

    list=[]

    for i in range(1, len(numero_str), 2):
        print(numero_str[i])
        list.append(int(numero_str[i]))
    
    return(list)
    

#Ejercicio 6
def sumar_digitos(lista_digitos : list[int]) -> int:
    l = [str(x) for x in lista_digitos]
    lista_digitos = []
    for x in l:
        lista_digitos.extend([int(e) for e in x])
    return sum(lista_digitos)

#Ejercicio 7
def luhn(numero_de_tarjeta :  str) -> bool:
    pares = digitos_pares(numero_de_tarjeta)
    suma_pares = sumar_digitos( [x* 2 for x in pares] )
    suma_impares = sum(digitos_impares(numero_de_tarjeta))
    dig = (suma_pares + suma_impares)%10
    return dig


#Ejercicio 8
def validar_tarjeta(numero_de_tarjeta : str) -> bool:
    return