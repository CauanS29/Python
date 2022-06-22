valores = input().split()  
A = float(valores[0]) 
B = float(valores[1]) 
C = float(valores[2]) 
pi = 3.14159 
areaTriangulo = ((A * C)/ 2) 
areaCirculo = pi * (C**2) 
areaTrapezio = ((A + B) * C) /2 
areaQuadrado = B * B 
areaRetangulo = A * B 
print("TRIANGULO:", "%.3f"% areaTriangulo)
print("CIRCULO:", "%.3f"% areaCirculo)
print("TRAPEZIO:", "%.3f"% areaTrapezio)
print("QUADRADO:", "%.3f"% areaQuadrado)
print("RETANGULO:", "%.3f"% areaRetangulo) 