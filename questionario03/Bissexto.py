ano = int(input()) 

serBissexto = "NAOBISSEXTO"

if ano%4 == 0 and (ano%100 != 0 or ano%400 == 0) : 
   serBissexto = "BISSEXTO" 

print(serBissexto)



#Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando ele com 366 dias, um dia a mais do que os anos normais de 365 dias, ocorrendo a cada quatro anos (exceto anos múltiplos de 100 que não são múltiplos de 400).

#Faça um programa que indique se o ano digitado é bissexto.
 
#Um número inteiro correspondendo ao ano. 

# Se o ano for bissexto imprima:

#BISSEXTO

#Caso não seja, imprima:

#NAOBISSEXTO

#(perceba que não tem o acento)
