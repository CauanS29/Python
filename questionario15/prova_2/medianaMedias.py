def media(listaNumeros): # mudei a função para cima do laço para poder dar o append na listaMedia 
 
    mediaNumeros = sum(listaNumeros)/(len(listaNumeros))# tireio -1 porque nao precisava e tirei a o append da função 

    return mediaNumeros


mediaLista = [] #criar lista vazia antes do laço
while True : 

    listaValores = input() #separei o split do input, porque dava erro na hora do break 
    
    if listaValores == "*":  
        break
    
    listaValores = listaValores.split(",") #esqueci de colocar a virgula no split

    listaValores = [float(i) for i in listaValores] # essa parte tinha que estar no laço

    mediaLista.append(media(listaValores)) #dar um append para cada media calculada


def medianaValores(listaNumeros, cont = 0 ): 


    valorMediana = 0 

    if len(listaNumeros) % 2 == 0: # troquei o cont pelo len da lista 
        
       cont = len(listaNumeros) // 2
       valorMediana = (listaNumeros[cont] + listaNumeros[cont - 1])/2 

    else: 
        cont = len(listaNumeros) - 1

        valorMediana = (listaNumeros[cont//2]) 

    return valorMediana 

mediaListaOrd = mediaLista.copy()  # criei uma copia da lista para poder ordenar ela de forma decrescente e criei uma variavel para guardar o valor da medianan
mediaListaOrd.sort(reverse = True) 
mediana = medianaValores(mediaListaOrd)

mediaLista = [str('%.2f' %i) for i in mediaLista]#transformei a lista em strings para poder limitar ela em duas casas decimais 
print(' '.join(mediaLista)) 
mediaListaOrd = [str('%.2f' %i) for i in mediaListaOrd]#transformei a lista em strings para poder limitar ela em duas casas decimais 
print(' '.join(mediaListaOrd))
print("Mediana das medias: %.2f" %mediana)

    
