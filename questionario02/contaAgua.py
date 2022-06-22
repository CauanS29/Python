agua = input().split()  
consumo = float(agua[0]) * 1000
custoAgua = float(agua[1]) * consumo 
valorEsgoto = custoAgua * 0.8 
valorTotal = custoAgua + valorEsgoto 
print("%.2f"%custoAgua) 
print("%.2f"%valorEsgoto)
print("%.2f"%valorTotal) 