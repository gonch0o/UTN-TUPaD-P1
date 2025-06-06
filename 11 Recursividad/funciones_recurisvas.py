#ejercicio 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
#if __name__ == "__main__":
#   print(factorial(5))

#ejercicio 2
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
#if __name__ == "__main__":
#    print(fibonacci(9))

#ejercicio 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
#if __name__ == "__main__":
#    print(potencia(5, 3))

#ejercicio 4
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
#if __name__ == "__main__":
#    print(f"Binario de 10 = {decimal_a_binario(10)}")

# ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])
#if __name__ == "__main__":
#    print(es_palindromo("oso"))  
#    print(es_palindromo("programacion"))    

# ejercicio 6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)
#if __name__ == "__main__":
#    print(suma_digitos(1234)) 

#ejercicio 7
def bloques(niveles):
    if niveles == 0:
        return 0
    else:
        return niveles + bloques(niveles - 1)
#if __name__ == "__main__":
#    print(bloques(5))


# ejercicio 8
def contar_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n // 10)

# prueba directa
if __name__ == "__main__":
    print(contar_digitos(645))