energiaConsumida = int(input()) 

valorKWh = 1.35

valorConta = energiaConsumida * valorKWh 

if valorConta <= 35 : 
    valorConta = 35 
  

if energiaConsumida >= 100 and energiaConsumida <= 299 :
   valorKWh = 1.55 
   valorConta = energiaConsumida * valorKWh 

elif energiaConsumida >= 300 and energiaConsumida <= 574 : 
    valorKWh = 1.75 
    valorConta = energiaConsumida * valorKWh * 1.10

elif energiaConsumida >= 575 : 
    valorKWh = 2.15 
    valorConta = energiaConsumida * valorKWh * 1.10 
 
print("%.2f"%valorConta)
print(valorKWh) 


