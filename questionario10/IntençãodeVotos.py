quantiadePesquisas = int(input()) 
candidato = input().split() 
concorrente= input().split() 

def vantagem(candidato, concorrente,quantiadePesquisas): 
    
    listaVantagem = []

    semVantangem = 0.00
   
    for i in range (0,quantiadePesquisas) : 

        if candidato[i] > concorrente[i] : 

           vantagem = float(candidato[i]) - float(concorrente[i]) 
           listaVantagem.append(vantagem)

        else : 

           listaVantagem.append(semVantangem) 

    return max(listaVantagem)
        

print("{:.2f}".format(vantagem(candidato, concorrente,quantiadePesquisas)))

