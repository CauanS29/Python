dias = int(input()) 
kmTotal = int(input()) 

valorDiaria = 90 * dias 

valorKm = dias * 100 

taxa = 0 

if kmTotal > valorKm : 
   taxa = 12 * (kmTotal - valorKm) 


valorTotal = valorDiaria + taxa 
print("%.2f"%valorTotal)

 



#A Locadora de Veículos lançouEudora  uma grande promoção esse mês: pagando apenas R$ 90 por diária, o cliente pode alugar um carro de passeio. Para cada diária, o cliente recebe uma cota de quilometragem de 100 Km. Cada quilômetro a mais custará uma taxa extra de R$ 12.  

#Escreva um programa que receba como entrada a quantidade de dias e a quilometragem total rodada por um cliente dessa locadora e exiba o valor total a ser pago com duas casas decimais.  

#Dois valores inteiros, separados por uma quebra de linha 

# Um valor real com duas casas decimais 