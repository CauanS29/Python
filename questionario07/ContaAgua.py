consumoAgua = int(input()) 

cont = 10

totalPagar = 7 

while cont <= consumoAgua : 

      if cont >= 11 and cont <= 30 : 
           totalPagar += 1 

      elif cont >= 31 and cont <= 100 : 
           totalPagar += 2 
     
      elif cont > 100 : 
           totalPagar += 5 
      
      cont += 1 


print(totalPagar) 
         
      

