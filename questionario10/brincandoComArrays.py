quantidadeNumeros = int(input())

listaNumeros = input().split() 


def Reversa(lista): 

    cont =  quantidadeNumeros - 1 

    listaNova = []

    while cont >= 0 : 

        listaNova.append(lista[cont]) 

        cont -= 1 
    
    texto = " ".join(listaNova) 

    return texto


def praEsquerda(lista, quantidadeNumeros) : 

    novaLista = lista[1:quantidadeNumeros] + [lista[0]] 
    
    texto = " ".join(novaLista) 

    return texto


print(Reversa(listaNumeros))

print(praEsquerda(listaNumeros,quantidadeNumeros)) 



numeros = [int(nomeNumero) for nomeNumero in listaNumeros]  

numeros.sort(reverse = True) 

converter = [str(nomeNumero) for nomeNumero in numeros]  

descrente = " ".join(converter) 

print(descrente) 



