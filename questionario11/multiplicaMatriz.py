quantidadeLinhaA, quantidadeLinhaB, quantidadeColunaB = input().split()
quantidadeLinhaA, quantidadeLinhaB, quantidadeColunaB = int(quantidadeLinhaA), int(quantidadeLinhaB), int(quantidadeColunaB)

matrizA = []
for _ in range(quantidadeLinhaA):
    linhaA = [int(x) for x in input().split()]
    matrizA.append(linhaA)

matrizB = []
for _ in range(quantidadeLinhaB):
    linhaB = [int(x) for x in input().split()]
    matrizB.append(linhaB)
    
def multiplicaMatriz(matrizA,matrizB):
    matrizC = []
    for lin in range(quantidadeLinhaA):
        matrizC.append([])
        for col in range(quantidadeColunaB):
            matrizC[lin].append(0)
            for j in range(quantidadeLinhaB):
                matrizC[lin][col] += matrizA[lin][j] * matrizB[j][col]
    return matrizC
    
matrizC = multiplicaMatriz(matrizA, matrizB)

for elem in matrizC:
    matrizStr = ''
    for num in elem:
        matrizStr += str(num) + ' '
    resultado = ' '.join(matrizStr.split())
    print(resultado)