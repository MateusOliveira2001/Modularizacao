valor = int(input('Insira um valor inteiro: '))

dobro = valor*2
metade = valor/2
fatorial = lambda x : x and x * fatorial(x-1) or 1
quadrado = valor**2
porcentagem = valor/10


print('-'*40)
print('\t\tRESULTADO')
print('-'*40)
print(f'O dobro de {valor} é igual a: \t{dobro}')
print(f'A metade de {valor} é igual a: \t{metade}')
print(f'O fatorial de {valor} é igual a: \t{fatorial(valor)}')
print(f'O quadrado de {valor} é igual a: \t{quadrado}')
print(f'10% de {valor} é igual a: \t\t{porcentagem}')
print('-'*40)

