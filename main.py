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
    x = digitos(numero_de_tarjeta)

    #for numero_par in numero_de_tarjeta:
        
    return

#Ejercicio 5
def digitos_pares(numero_de_tarjeta: str) -> list[int]:
    return

#Ejercicio 6
def sumar_digitos(lista_digitos : list[int]) -> int:
    return

#Ejercicio 7
def luhn(numero_de_tarjeta :  str) -> bool:
    return

#Ejercicio 8
def validar_tarjeta(numero_de_tarjeta : str) -> bool:
    return