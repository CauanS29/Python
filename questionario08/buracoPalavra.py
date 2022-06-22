numeroLeituras = int(input()) 

for i in  range(0, numeroLeituras) : 

    palavra = input().upper()

    cont = 0

    for letra in palavra :
      
        if letra in "ADOPRQ" : 
           cont += 1 

        elif letra in "B" : 
             cont += 2 

    print(cont) 