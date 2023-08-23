def dobro(valor):
    d = valor*2
    return d


def metade(valor):
    m = valor/2
    return m


def fatorial(valor):
    f = 1
    for n in range (1,valor+1):
        f *= n
    return f

def quadrado(valor):
    q = valor**2
    return q


def porcentagem(valor):
    p = valor/10
    return p


def imprime(valor):
    print('-'*40)
    print('\t\tRESULTADO')
    print('-'*40)
    print(f'O dobro de {valor} é igual a: \t{dobro(valor)}')
    print(f'A metade de {valor} é igual a: \t{metade(valor)}')
    print(f'O fatorial de {valor} é igual a: \t{fatorial(valor)}')
    print(f'O quadrado de {valor} é igual a: \t{quadrado(valor)}')
    print(f'10% de {valor} é igual a: \t\t{porcentagem(valor)}')
    print('-'*40)

valor = int(input('Insira um valor inteiro: '))

imprime(valor)