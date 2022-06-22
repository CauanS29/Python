numero = float(input()) 

def intervalo (numero) : 
    numeroIntervalo = "Intervalo (25,50]"
    
    if numero >= 0 and numero <= 25 : 
       numeroIntervalo = "Intervalo [0,25]" 

    elif numero > 50 and numero <= 75 : 
          numeroIntervalo = "Intervalo (50,75]" 

    elif numero > 75 and numero <= 100 : 
         numeroIntervalo = "Intervalo (75,100]" 

    elif numero < 0 or numero > 100 : 
         numeroIntervalo = "Fora de intervalo"

    return numeroIntervalo  

print(intervalo(numero))