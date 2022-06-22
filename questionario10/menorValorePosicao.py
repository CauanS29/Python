tamanhoArray = int(input()) 

listaNumeros = input().split() 

numeros = [int(nomeNumero) for nomeNumero in listaNumeros] 

menorNumero = min(numeros) 

posicao = (numeros.index(menorNumero)) 

print("Menor valor:", menorNumero) 
print("Posicao:", posicao) 