def EstacaoAnoSul (hemisferio,dia, mes) : 
    if  (hemisferio == 1) and (dia >= 21 and mes == 12) or (mes == 1 or mes == 2) or (dia <= 20 and mes == 3) : 
        return "VERAO"  

    elif (hemisferio == 1) and (dia >= 21 and mes == 3) or (mes == 4 or mes == 5) or (dia <= 20 and mes == 6) : 
        return "OUTONO" 

    elif (hemisferio == 1) and  (dia >= 21 and mes == 6) or (mes == 7 or mes == 8) or (dia <= 20 and mes == 9) : 
        return "INVERNO"
    
    elif (hemisferio == 1) and (dia >= 21 and mes == 9) or (mes == 10 or mes == 11) or (dia <= 20 and mes == 12) : 
        return "PRIMAVERA"  


def EstacaoAnoNorte (hemisferio,dia, mes) : 
    if  (hemisferio == 0) and (dia >= 21 and mes == 12) or (mes == 1 or mes == 2) or (dia <= 20 and mes == 3) : 
        return "INVERNO"  

    elif (hemisferio == 0) and (dia >= 21 and mes == 3) or (mes == 4 or mes == 5) or (dia <= 20 and mes == 6) : 
        return "PRIMAVERA" 

    elif (hemisferio == 0) and  (dia >= 21 and mes == 6) or (mes == 7 or mes == 8) or (dia <= 20 and mes == 9) : 
        return "VERAO"
    
    elif (hemisferio == 0) and (dia >= 21 and mes == 9) or (mes == 10 or mes == 11) or (dia <= 20 and mes == 12) : 
        return "OUTONO"  


hemisferio = int(input()) 
dia = int(input()) 
mes = int(input())

if hemisferio == 0 : 
   print(EstacaoAnoNorte(hemisferio, dia, mes)) 
else : 
   print(EstacaoAnoSul(hemisferio, dia, mes))