
def fibonacci(limit):
    print('Vou tentar criar o bagulho do Fibonacci')
    listaFibonacci = [0,1]
    a, b = 0,1
    while a < limit:
        c = a + b
        listaFibonacci.append(a)
        a = b
        b = c
        listaFibonacci.append(c)
        
    return listaFibonacci
listaFib = fibonacci(100)

print(listaFib)