def soPositivo(listaNumeros, i =0): 

    if(listaNumeros[i] < 0) : 
        return False 

    else: 
        if(i == len(listaNumeros) - 1): 
         return True 

    return soPositivo(listaNumeros, i + 1)


listaNumeros = input().split() 
listaNumeros = [int(i) for i in listaNumeros] 

def entre5e10(listaNumeros, i = 0, cont = 0): 

    if(i == len(listaNumeros)): 
        return cont 

    if(listaNumeros[i] >= 5 and listaNumeros[i] <= 10): 
        return entre5e10(listaNumeros, i + 1, cont + 1)
    
    else: 
        return entre5e10(listaNumeros, i + 1, cont) 