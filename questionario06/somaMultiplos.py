num = int(input()) 

cont = 0

soma = 0

while cont < num : 
    if cont%3 == 0 or cont%5 == 0 : 
       soma = cont + soma 

    cont =  cont + 1 

print(soma)