def vencedorVotacao(quantidadeVotosNulo, quantidadeVotosNao, quantidadeVotosSim) : 
    
    vencedor = "SEM FOGOS" 

    if quantidadeVotosSim > quantidadeVotosNao + quantidadeVotosNulo : 
       vencedor ="COM FOGOS" 

    return vencedor
    

quantidadeVotosNulo = 0

quantidadeVotosNao = 0

quantidadeVotosSim = 0

while 2 > 1 : 
     voto = input() 

     if voto == "encerrar" or voto == "Encerrar" or "ENCERRAR" : 
           break

     if voto == "sim" : 
        quantidadeVotosSim += 1 

     elif voto == "Sim" : 
        quantidadeVotosSim += 1 
     
     elif voto == "SIM" : 
        quantidadeVotosSim += 1 

   
     elif voto == "nao" : 
        quantidadeVotosNao += 1 
     
     elif voto == "NAO" : 
        quantidadeVotosNao += 1 

     elif voto == "Nao" : 
        quantidadeVotosNao += 1 
     
     elif voto == "Nulo" : 
         quantidadeVotosNulo += 1 

     elif voto == "nulo" : 
         quantidadeVotosNulo += 1 

     elif voto == "NULO" : 
         quantidadeVotosNulo += 1 


print(vencedorVotacao(quantidadeVotosNulo, quantidadeVotosNao, quantidadeVotosSim))