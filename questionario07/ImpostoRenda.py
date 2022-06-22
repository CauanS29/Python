salario = float(input()) 

diferenca = 0 

cont = salario - 1

impostoPagar = 0

while cont < salario : 

      if cont >= 2000.01  and cont <= 3000.00 : 
           impostoPagar += (salario - 2000) * 0.08 
                

      elif cont > 3000 and cont <= 4500.00 : 
           impostoPagar += (1000 * 0.08) 
           impostoPagar += (salario - 3000) * 0.18 
                    

      elif cont > 4500.00 : 
           impostoPagar += (1000 * 0.08) 
           impostoPagar += (1500 * 0.18) 
           impostoPagar += (salario - 4500) * 0.28
                     

      cont += 1 
                

if impostoPagar == 0 : 
   print("Isento") 

else : 
    print("R$ %.2f"%impostoPagar)







