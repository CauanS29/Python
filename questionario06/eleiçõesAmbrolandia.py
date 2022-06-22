

votosAlibaba = 0 
votosAlcapone = 0 
votosBranco = 0 
votosNulo = 0 
vencedor = 83 



while 1 > 0 : 
    valorVotado = int(input())  
    if(valorVotado < 0) : 
       break

    if valorVotado == 83 : 
       votosAlibaba += 1
    
    elif valorVotado == 93 : 
       votosAlcapone += 1 

    elif valorVotado == 0 : 
        votosBranco += 1 

    else : 
        votosNulo += 1  

if votosAlcapone >= votosAlibaba : 
   vencedor = 93 

totalVotos = votosAlcapone + votosAlibaba + votosBranco 

percentualVotosAlcapone = (votosAlcapone * 100)/totalVotos 
percentalVotosAlibaba = (votosAlibaba * 100)/totalVotos 


print(votosAlibaba) 
print(votosAlcapone) 
print(votosBranco)  
print(votosNulo) 
print(vencedor) 
print("%.2f"%percentalVotosAlibaba)
print("%.2f"%percentualVotosAlcapone)