quantidadeNotas = int(input()) 

listaNotas = []

for i in range(0, quantidadeNotas): 
    
    notas = float(input()) 
    
    listaNotas.append(notas)

  


media = sum(listaNotas)/quantidadeNotas 

acimaMedia = media + (media * 0.1) 

abaixoMedia = media - (media * 0.1) 

def quantosAcima (media, acimaMedia): 

    cont = 0 

    for i in media : 

        if i > acimaMedia : 
            cont += 1 

    return cont 


def quantosAbaixo (media, abaixoMedia): 

    cont = 0 

    for i in media : 

        if i < abaixoMedia : 
            cont += 1 

    return cont 



print("%.2f"%media) 
print(quantosAcima(listaNotas, acimaMedia)) 
print(quantosAbaixo(listaNotas, abaixoMedia))
