# Practica 9: Hacer la serie de Fibonacci N numeros.

def fibonacci(n):
    if n in {0, 1}:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2) 

for i in range(20):
    print(fibonacci(i), end=" ")
