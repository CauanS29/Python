diagonal = input()
limiar = int(input())
n = int(input())

matriz = []
for _ in range(n):
    linha = [int(x) for x in input().split()]
    matriz.append(linha)

def somaAcima(matriz):
    soma = 0
    for i in range(n):
        for j in range(i+1, len(matriz[i])):
            soma += matriz[i][j]
    return soma 

def somaAbaixo(matriz):
    soma = 0
    for i in range(n):
        for j in range(len(matriz[i])):
            if i > j:
                soma += matriz[i][j]
    return soma 

def limiarMaior(matriz, limiar):
    p = False
    if diagonal == 'acima':
        if somaAcima(matriz) > limiar:
            p = True
    elif diagonal == 'abaixo':
        if somaAbaixo(matriz) > limiar:
            p = True
    return p

resultado = limiarMaior(matriz, limiar)

print(resultado)