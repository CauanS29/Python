def ehVogal(palavra1): 

    restoPalavra = ""

    for i in palavra1 : 

        if i in "aeiou" : 
           restoPalavra += i 

    return restoPalavra


def ehPalindromo(palavra1): 

    return ehVogal(palavra1) == ehVogal(palavra1[::-1])  


QuantidadeTestes = int(input()) 


for i in range(0, QuantidadeTestes):  


    risada = input().lower() 

    if  len(risada) > 50 or ehVogal(risada) == "" : 
        print("INVALIDA") 
        continue 

    if ehPalindromo(risada) : 
       print("ENGRACADA")

    else : 
       print("SEM GRACA") 
            


