listaNumeros = input().split() 

quantiadeLeituras = int(listaNumeros[0])

listaNomes = []

for i in range(0, quantiadeLeituras):  

    nome = input() 

    listaNomes.append(nome) 

listaNomes.sort()

vencedor = int(listaNumeros[1]) 

felizardo = listaNomes[vencedor - 1]

print(felizardo)