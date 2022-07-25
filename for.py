words = ['Eu','sou', 'calvo', ';-;']

obj = {
    'Nome' : 'Carlos',
    'Idade' : '24 anos',
    'Profissao' : 'Programador Jr',
    'Especializações' : [
        'Node JS',
        'Php',
        'Gana'
    ]
} 

def lista100():
    return list(range(100))


def isPrimeNumber(num):
    isPrimo = True
    for current in range(2,num):
        if ((num % current) == 0 and num != current )  :
            return False
    return isPrimo 


def listaDePrimos(tamanhoDaLista):
    lista = list(range(2,tamanhoDaLista))
    listaDePrimos = []
    for current in lista :
        if(isPrimeNumber(current)):
            listaDePrimos.append(current)
            
    return listaDePrimos
            
        
numeroEhPrimo = isPrimeNumber(11)

listaPrimos = listaDePrimos(550)

print(listaPrimos)

