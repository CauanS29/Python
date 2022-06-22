tamanho = input().split()
linha = int(tamanho[0])
coluna = int(tamanho[1])

somaLista = []
for _ in range(linha):
    lista = []
    lista = [int(x) for x in input().split()]
    j = coluna - 1
    soma = 1
    listasequencias = []
    for i in range(j):
        if lista[i] <= lista[i + 1]:
            soma += 1
        else:
            listasequencias.append(soma)
            soma = 1
    listasequencias.append(soma)
    maiorsequencia = 0
    maiorsequencia = None
    for k in listasequencias:
        if maiorsequencia is None:
            maiorsequencia = k
        elif k > maiorsequencia:
            maiorsequencia = k


    somaLista.append(maiorsequencia)

for a in range(len(somaLista)):
    print(f'Linha {a}: {somaLista[a]}')

maior = None
for b in somaLista:
    if maior is None:
        maior = b
    elif b > maior:
        maior = b

print('Maior Sequencia:', maior)