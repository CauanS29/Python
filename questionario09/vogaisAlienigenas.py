def contar_vogais(vogais, fraseVogais): 

    cont = 0 

    for i in fraseVogais : 
    
       if i in vogais :
          cont += 1

    return cont   


numeroTestes = int(input()) 


for i in range(0, numeroTestes): 
    
    vogais = input() 
    fraseVogais = input() 
    print(contar_vogais(vogais, fraseVogais))


