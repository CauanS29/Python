diametro = int(input()) 
medidas = input().split() 
altura = float(medidas[0]) 
largura = float(medidas[1]) 
profundidade = float(medidas[2]) 

cabe = "S"

if diametro > largura or diametro > altura or diametro > profundidade :
   cabe = "N" 

print(cabe)




#A Copa do Mundo de 2010 foi realizada na Africa do Sul. Bolas de futebol são muito fáceis de transportar, já que elas saem das fábricas vazias e só são enchidas somente pelas lojas ou pelos consumidores finais. Infelizmente o mesmo não pode ser dito das bolas de boliche. Como elas são completamente sólidas, elas só podem ser transportadas embaladas uma a uma, em caixas separadas. 

#A Ambroliche é uma fábrica de bolas de boliche que trabalha somente através de encomendas e envia todas as bolas por SEDEX. Como as bolas têm tamanhos diferentes, a Ambroliche tem vários tamanhos de caixas diferentes para transportá-las.

#Escreva um programa que, dado o diâmetro de uma bola e as 3 dimensões de uma caixa (altura, largura e profundidade), diz se a bola de boliche cabe dentro da caixa ou não. 

#A primeira linha da entrada contém um inteiro N (1 <= N <= 10.000) que indica o diâmetro da bola de boliche. A segunda linha da entrada contém 3 números inteiros separados por um espaço cada: a altura A (1 <= A <= 10.000), seguida da largura L (1 <= L <= 10.000) e da profundidade P (1 <= P <= 10.000).  

#Seu programa deve imprimir uma única linha, contendo a letra 'S' caso a bola de boliche caiba dentro da caixa ou 'N' caso contrário. 
