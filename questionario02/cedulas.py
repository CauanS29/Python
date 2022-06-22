valor = int(input()) 

cedulas100 = valor//100  
valor100 = valor%100  
cedulas50 = valor100//50 
valor50 = valor100%50 
cedulas20 = valor50//20  
valor20 = valor50%20 
cedulas10 = valor20//10 
valor10 = valor20%10 
cedulas5 = valor10//5 
valor5 = valor10%5 
cedulas2 = valor5//2  
valor2 = valor5%2 
cedulas1 = valor2//1  


print(valor)
print(cedulas100, "nota(s) de R$ 100,00") 
print(cedulas50, "nota(s) de R$ 50,00") 
print(cedulas20, "nota(s) de R$ 20,00" ) 
print(cedulas10, "nota(s) de R$ 10,00")  
print(cedulas5,"nota(s) de R$ 5,00" )
print(cedulas2, "nota(s) de R$ 2,00") 
print(cedulas1, "nota(s) de R$ 1,00")


