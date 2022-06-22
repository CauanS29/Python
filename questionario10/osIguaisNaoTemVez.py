quantidadeEntrada = int(input()) 

listaNumeros = input().split() 


def compara(numero) : 

    lista = [] 

    for i in numero : 

        if int(i) not in lista :  

         lista.append(int(i))
    

    return(lista) 

listaSemRepetir = compara(listaNumeros) 

listaSemRepetir.sort()


numeros = [str(nomeNumero) for nomeNumero in listaSemRepetir] 

texto = " ".join(numeros) 

print(texto)


        