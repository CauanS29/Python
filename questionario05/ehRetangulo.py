
def eRetangulo (lado1, lado2, lado3, lado4) : 
    if lado1 == lado2 and lado3 == lado4 : 
       return "RETANGULO" 
 
    elif lado1 == lado3 and lado2 == lado4 : 
         return "RETANGULO" 

    elif lado1 == lado4 and lado3 == lado2 : 
         return "RETANGULO" 
    
    else : 
        return "NAO EH UM RETANGULO" 
       
lado1 = int(input()) 
lado2 = int(input()) 
lado3 = int(input()) 
lado4 = int(input())  

print(eRetangulo(lado1, lado2, lado3, lado4))