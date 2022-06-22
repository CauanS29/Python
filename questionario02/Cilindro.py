altura = float(input()) 
raio = float(input()) 
pi = 3.14  
volumeCilindro = pi * (raio * raio) * altura 
areaSuperficie = 2 * pi * raio * altura + 2 * pi * (raio * raio) 
print("%.2f"%volumeCilindro) 
print("%.2f"%areaSuperficie)

# O volume de um cilindro é π r² h, e sua área de superfície é 2π r h + 2π r².