def removeCaracteres(texto): 

    palavraNormal = "" 

    for letra in texto: 

        if(letra not in '."(*$#:'): 
            palavraNormal += letra 

    return palavraNormal

dicionarioPalavras = dict() 

while True : 

    texto = input()
    
    if texto == "-1": 
        break 
    if texto == "":
        continue 
    
    palavras = removeCaracteres(texto)
    palavras = palavras.lower().split() 

    for palavra in palavras:
        dicionarioPalavras[palavra] = dicionarioPalavras.get(palavra, 0) + 1 

    dicionarioPalavras = sorted(dicionarioPalavras.items())


for palavraDic, aparicao in dicionarioPalavras: 
     print(palavraDic,"-",aparicao) 





