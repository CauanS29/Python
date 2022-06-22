idadeNadador = int(input()) 

categoriaNadador = "Idade invalida." 

if idadeNadador >= 5 and idadeNadador <=7 : 
   categoriaNadador = "Infantil A" 

elif idadeNadador >= 8 and idadeNadador <= 10 : 
     categoriaNadador = "Infantil B" 

elif idadeNadador >= 11 and idadeNadador <= 13 : 
     categoriaNadador = "Juvenil A" 

elif idadeNadador >= 14 and idadeNadador <= 17 : 
     categoriaNadador = "Juvenil B" 

elif idadeNadador >= 18 and idadeNadador <= 40 : 
     categoriaNadador = "Adulto" 

elif idadeNadador >= 41 : 
     categoriaNadador = "Master" 

print(categoriaNadador)