def fibonacci(limit):
    listaFibonacci = [0,1]
    a, b = 0,1
    while a < limit:
        c = a + b
        listaFibonacci.append(a)
        a = b
        b = c
        
    return listaFibonacci
