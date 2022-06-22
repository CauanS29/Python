listaConvidados = []

while True : 
    
    convidado = input()
    
    if convidado == "FIM" : 
            break 
    
    else : 
        listaConvidados.append(convidado)
     
    
while 2 > 1 : 

    listaConvidados.sort() 

    for i in listaConvidados : 

        print(i) 

    numeroConvidados = int(input()) 
      
    if numeroConvidados == 0 : 
          break 

    print("--------------------------------------------------") 

    for i in range(0, numeroConvidados) :

        novosConvidados = input() 

        listaConvidados.append(novosConvidados) 
    

    
    