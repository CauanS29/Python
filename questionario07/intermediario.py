numero1 = int(input()) 
numero2 = int(input()) 
numero3 = int(input()) 

def oMaior (num1, num2,num3) : 
    maior = max(num1, num2, num3) 
    return maior 

def oMenor (num1, num2,num3) : 
    menor = min(num1, num2, num3)
    return menor


def intermediario(numero1, numero2, numero3) :
    maiorValor = oMaior(numero1, numero2, numero3) 
    menorValor = oMenor(numero1, numero2, numero3) 
    
    intermediario = numero2 

    if numero1 != maiorValor and numero1 != menorValor : 
       intermediario = numero1 
     
    elif numero3 != maiorValor and numero3 != menorValor : 
       intermediario = numero3 

    return intermediario


print(intermediario(numero1, numero2, numero3)) 