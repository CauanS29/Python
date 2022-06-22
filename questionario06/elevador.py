valores = input().split()

numeroLeituras = int(valores[0])
capacidadeMaxima = int(valores[1]) 

sensor = 0 

condicaoCapacidade = "N"

elevador = 0 

while sensor < numeroLeituras : 
      valoresCapacidade = input().split() 

      S = int(valoresCapacidade[0]) 
      E = int(valoresCapacidade[1])  

      elevador = elevador - S 

      elevador = elevador + E 

      if  elevador > capacidadeMaxima : 
         condicaoCapacidade = "S" 

      sensor += 1 


print(condicaoCapacidade) 
