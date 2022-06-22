def oMaior (num1, num2) : 
    maior = num1 
     
    if num2 > num1 : 
        maior = num2 

    return maior 


def oMenor (num1, num2) : 
    menor = num1 

    if num2 < num1 : 
       menor = num2 

    return menor


num1 = int(input()) 
num2 = int(input()) 

extremidadeFinal = oMaior(num1,num2) 
extremidadeInicial = oMenor(num1, num2)  
 
soma = 0 

while extremidadeInicial <= extremidadeFinal : 
    
    if extremidadeInicial > 0 : 
        soma += extremidadeInicial
     
    extremidadeInicial += 1 


print(soma)
   


      