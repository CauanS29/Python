listaNumeros = input().split() 

def contaAparicoes(numero) : 
 
    listaNova = [] 

    listaNova.append(numero[-1])

    for i in numero : 

        if i in listaNova :  

         listaNova.append(i)

    aparicoes = len(listaNova) - 1 

    return aparicoes 

numeroRepete = listaNumeros[-1] 

print("O numero", numeroRepete, "apareceu", contaAparicoes(listaNumeros), "vezes")