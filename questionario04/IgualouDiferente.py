numero1 = int(input()) 
numero2 = int(input()) 
numero3 = int(input()) 

situacaoNumero = 3 

if numero1 == numero2 and numero2 == numero3 : 
   situacaoNumero =  1 

elif numero1 != numero2 and numero1 != numero3 and numero2 !=  numero3 : 
   situacaoNumero = 2 

print(situacaoNumero)