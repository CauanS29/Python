cont = 0
 
valorCofrinho = 0

metasBatidas = 0 

valorAnterior = 99999999999999

while cont < 7 :  
      valorDeposito = float(input()) 
      valorCofrinho = valorCofrinho + valorDeposito 

      if valorDeposito >= (valorAnterior + 0.5) : 
         metasBatidas += 1 

      valorAnterior = valorDeposito 

        
      cont += 1 

print("R$ %.2f"%(valorCofrinho)) 
print(metasBatidas)
