palavra1 = input() 
palavra2 = input() 

restoLetras = ""

for i in palavra1 : 

    if i not in palavra2 : 
       restoLetras += i 
       
    else : 
       continue

print(restoLetras)
    