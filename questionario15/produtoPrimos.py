def ehPrimo(num, i = 2):

    if (num <= 2):
        return True if(num == 2) else False
    if (num % i == 0):
        return False
    if (i * i > num):
        return True
    
    return ehPrimo(num, i + 1)

numeros = input().split()  

transformaNumeros = []

for i in numeros : 

    transformaNumeros.append(int(i))


resultado = 1

cont = 0

for i in transformaNumeros :

   if  ehPrimo(i) : 

       resultado *= i 
    
       cont += 1 


if cont == 4 : 

    print(resultado) 

else : 
    print("SEM PRODUTO")
    




       

    

    