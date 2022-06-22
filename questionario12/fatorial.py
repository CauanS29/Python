def calculaFatorial (valor): 
    
    if valor == 1 or valor == 0 : 
        return 1 

    else : 
         
       fatorial = valor * calculaFatorial(valor -1) 

       return fatorial


while True : 

    valor = int(input()) 

    if valor == -1 : 
        break 

    print(calculaFatorial(valor)) 
