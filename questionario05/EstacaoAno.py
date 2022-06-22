def EstacaoAno (dia, mes) : 
    if (dia >= 21 and mes == 12) or (mes == 1 or mes == 2) or (dia <= 20 and mes == 3) : 
        return "VERAO"  

    elif (dia >= 21 and mes == 3) or (mes == 4 or mes == 5) or (dia <= 20 and mes == 6) : 
        return "OUTONO" 

    elif (dia >= 21 and mes == 6) or (mes == 7 or mes == 8) or (dia <= 20 and mes == 9) : 
        return "INVERNO"
    
    elif (dia >= 21 and mes == 9) or (mes == 10 or mes == 11) or (dia <= 20 and mes == 12) : 
        return "PRIMAVERA"  

dia = int(input()) 
mes = int(input())

print(EstacaoAno(dia, mes))