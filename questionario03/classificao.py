pontos1 = int(input()) 
pontos2 = int(input()) 
pontos3 = int(input()) 
pontos4 = int(input()) 
pontos5 = int(input())
pontos6 = int(input()) 

condicao = "Eliminado" 

if  (pontos1 + pontos2 + pontos3 + pontos4 + pontos5 + pontos6) >= 100 : 
    condicao = "Classificado" 

print(condicao)


#Este mês ocorre o Mundial de Tiro Ao Alvo e as competições ocorrem em duas etapas. Para se classificar para a segunda etapa, cada competidor precisa somar pelo menos 100 pontos ao longo de 6 partidas. Escreva um programa que receba como entrada os pontos feitos por um competidor em cada uma das partidas da primeira etapa, e exiba uma mensagem informando se ele foi classificado ou não.  

# Seis números inteiros, cada um representando a pontuação do jogador em uma partida. 

# Um String com a mensagem Classificado ou Eliminado, de acordo com a pontuação total do competidor. 