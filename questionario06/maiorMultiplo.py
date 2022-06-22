num1 = int(input()) 
num2 = int(input()) 

cont = num1 

multiplo = 0

if num1 > num2 : 
   multiplo = "sem multiplos menores que " + str(num2) 
   
else: 
      while (cont <= num2) : 
          if cont%num1 == 0 : 
             multiplo = cont 
          cont += 1 

print(multiplo) 