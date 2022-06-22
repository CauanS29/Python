kwh = 1.50 
consumo = float(input()) 
consumoTotal =  (kwh * consumo )
consumoDesconto = (consumoTotal * 0.85)
print("Valor a ser pago: R$", "%.2f"%consumoTotal, "reais")  
print("Valor a ser pago com desconto: R$", "%.2f"%consumoDesconto, "reais")


#Valor a ser pago: R$ 24.80 reais
#Valor a ser pago com desconto: R$ 21.08 reais