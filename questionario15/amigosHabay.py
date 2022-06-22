inscricoes = {} 

while True:
    try:
        nome,vontade = input().split()
        inscricoes[nome] = vontade
    except:
        break

querAmizade = [] 

naoQuerAmizade = [] 

for nome,vontade in inscricoes.items(): 

    if vontade == "SIM" : 
        querAmizade.append(nome) 

    else : 
        naoQuerAmizade.append(nome) 

maiorNome = 0 
vencedor = ""
for amigo in querAmizade: 

    if len(amigo) > maiorNome :
        maiorNome = len(amigo) 
        vencedor = amigo

querAmizade.sort() 
naoQuerAmizade.sort() 



[print(inscrito) for inscrito in querAmizade + naoQuerAmizade] 
print("\nAmigo do Habay:")
print(vencedor)