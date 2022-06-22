tipoMedia = input() 
numero1 = int(input()) 
numero2 = int(input()) 
numero3 = int(input()) 


media = (numero1 + numero2 + numero3)/3 


if tipoMedia == "G" : 
   media = (numero1 * numero2 * numero3) ** (1/3) 

if tipoMedia == "H" : 
   media = 3/ ((1/numero1) + (1/numero2) + (1/numero3))  

print("%.3f"%media)

