numero = int(input()) 

if numero > 0 : 
   unidade = numero%10 

if numero <=0 : 
   numero = numero * (-1)
   unidade = numero%10 
   unidade = unidade * (-1) 

print(unidade)  

#Escreva um programa que recebe um numero inteiro como entrada e fornece o algarismo da casa das unidades deste numero.

#Por exemplo, o algarismo da casa das unidades do número 3872 é 2.

#Se o número dado for negativo, considere que o algarismo também será negativo. Por exemplo, se o número dado for -74, a resposta deve ser -4 e não 4.

