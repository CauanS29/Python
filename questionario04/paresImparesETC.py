
n = int(input())

if n%2 == 0 and n > 0 : 
   print("POSITIVO PAR") 

elif n%2 != 0 and n > 0 : 
     print("POSITIVO IMPAR") 

elif n < 0 and n%2 == 0 : 
     print("NEGATIVO PAR") 

elif n < 0 and n%2 != 0 : 
     print("NEGATIVO IMPAR") 

else : 
     print("NULO")




'''Leia um valor inteiro n. Depois, imprima uma mensagem dizendo que se este valor for ímpar, par, positivo, negativo ou nulo.
A mensagem deve estar em letras maiúsculas. 

Um número n.
Considere que o maior inteiro que você poderá receber é 10^12 (10 elevado a 12)

Uma frase, informando se o número é POSITIVO PAR, POSITIVO IMPAR, NEGATIVO PAR, NEGATIVO IMPAR ou NULO.

Seguido de uma quebra de linha.'''