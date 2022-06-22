numero1 = int(input()) 
numero2 = int(input()) 
numero3 = int(input()) 

menor = numero2 

if numero1 <= numero2 and numero1 <= numero3 : 
   menor = numero1 

if numero3 <= numero2 and numero3 <= numero1 : 
   menor = numero3 

print(menor)
 
#Faça um programa que leia 3 números inteiros e imprima o menor deles. 

#03 números inteiros separados por um final de linha. 

#O menor dos números digitados. 