from funciones_recurisvas import factorial, fibonacci, potencia, decimal_a_binario, es_palindromo, suma_digitos, bloques, contar_digitos

#ejercicio 1
numero = int(input("ingrese un numero para calcular factoriales desde 1 hasta ese numero: "))
for i in range(1, numero + 1):
    print(f"{i}! = {factorial(i)}")

#ejercicio 2
pos = int(input("\ningrese una posición para mostrar la serie de fibonacci hasta esa posicion: "))
for i in range(pos + 1):
    print(f"fibonacci({i}) = {fibonacci(i)}")

#ejercicio3 
base = int(input("\ningrese la base: "))
exponente = int(input("ingrese el exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")

#ejercicio 4
decimal = int(input("\ningrese un numero decimal para convertir a binario: "))
binario = decimal_a_binario(decimal)
print(f"{decimal} en binario es {binario or '0'}")

#ejercicio 5
palabra = input("\ningrese una palabra para verificar si es un palindromo: ")
if es_palindromo(palabra):
    print(f"'{palabra}' es un palindromo.")
else:
    print(f"'{palabra}' NO es un palindromo.")

#ejercicio 6
numero = int(input("\ningrese un numero para sumar sus digitos: "))
print(f"la suma de los digitos de {numero} es {suma_digitos(numero)}")    

#ejercicio 7
niveles = int(input("\ningrese el numero de niveles de la piramide: "))
print(f"se necesitan {bloques(niveles)} bloques para una piramide de {niveles} niveles.")

#ejercicio 8
numero = int(input("\ningrese un numero para contar sus digitos: "))
print(f"{numero} tiene {contar_digitos(numero)} digitos.")