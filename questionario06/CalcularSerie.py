numeroRepeticoes = float(input())

numerador = 1 

denominador = 3

texto = ""

resultado = 0 

while numerador <= numeroRepeticoes : 
     
     if numerador == numeroRepeticoes : 
        calculo = (str(numerador) + "/" + str(denominador * numerador)) 
     else : 

        calculo = (str(numerador) + "/" + str(denominador * numerador) + " + ") 

     texto += calculo

     resultado = resultado + (numerador/(denominador * numerador))

    

     numerador += 1 
     


print(texto) 
print("%.2f"%resultado)