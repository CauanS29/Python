lado1 = float(input()) 
lado2 = float(input())
lado3 = float(input()) 

igualdade = "isosceles" 

if lado1 == lado2 and lado2 == lado3 : 
   igualdade = "equilatero"  

elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3 :
    igualdade = "escaleno" 

print(igualdade) 