listaNumeros = [] 

for i in range (0, 101) : 

    numero = int(input()) 
    listaNumeros.append(numero) 


numero101 = listaNumeros[-1] 

cont = 0 

for i in listaNumeros : 
    
    if i == numero101 and cont != 100 : 
        print(cont) 
    
    cont += 1