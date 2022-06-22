tamanhoArray = int(input()) 

listaArray1 = [] 

listaArray2 = []

listaIntercalados = [] 

for i in range (0, tamanhoArray) : 

    numerosArray1 = int(input()) 

    listaArray1.append(numerosArray1) 

for j in range (0, tamanhoArray) : 

    numerosArray2 = int(input()) 

    listaArray2.append(numerosArray2) 

   
for k in range (0, tamanhoArray) : 

    listaIntercalados.append(listaArray1[k])
 
    listaIntercalados.append(listaArray2[k]) 


for z in listaIntercalados : 

    print(z) 