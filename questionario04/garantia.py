valorProduto = float(input()) 
tempoGarantia = int(input()) 

garantia1ano = (valorProduto * 1.03) 

garantia2anos = (valorProduto * 1.05) 

if tempoGarantia == 1 : 
   print("%.2f"%garantia1ano) 

elif tempoGarantia == 2 : 
     print("%.2f"%garantia2anos) 

else : 
    print("%.2f"%valorProduto)







#A Favorita vende eletrodomésticos e eletroeletrônicos, e oferece a seus clientes a opção de comprar também a garantia estendida. Se quiserem apenas a garantia simples, os clientes não pagam nada a mais, apenas o valor do produto. Caso optem pela garantia estendida de um ano, deverão pagar uma taxa extra de 3% do valor do produto. Já a garantia estendida de dois anos custa 5% do valor do produto.

#Escreva um programa para essa loja que receba como entrada o valor do produto comprado e a quantidade de anos de garantia estendida desejados, e exiba o valor total a ser pago.

#Dica: Caso o cliente não queira garantia estendida, ele indicará 0 anos.  


#Um valor real, seguido por um valor inteiro 

#Um valor real com duas casas decimais 