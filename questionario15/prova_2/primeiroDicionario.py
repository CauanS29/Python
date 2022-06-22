def remover_especiais(palavra): 

    palavraLimpa = "" 

    for i in palavra: 
        
        if i not in '".(*$#:': #esqueci de usar o ponto 
           palavraLimpa += i 

    return palavraLimpa 


dicionariopalavras = dict() #esqueci de colocar o t da palavra dict 


while True : 

    palavra = input() 

    if palavra == '-1': 
         break 

    if palavra =='': 
       continue 

    palavra = remover_especiais(palavra) #faltou tirar os caracteres especias usando a função remove_especiais para depois poder usar o lower e split
    palavra = palavra.lower().split() 


    for letra in palavra : 
        dicionariopalavras[letra] = dicionariopalavras.get(letra, 0) + 1 


    dicionariopalvrasOrd = sorted(dicionariopalavras.items()) # precisei trocar a ordenacao de lugar com o .get(), pois dava erro , provavelmente porque ele nao tinha nada para ordenar 


for palavras, posicao in dicionariopalvrasOrd: 

    print(palavras, "-",posicao) #esqueci de usar o for para dar o print final



    