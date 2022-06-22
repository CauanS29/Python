def ehMultiplos(numero1, numero2):
    cont = 1
    totalMultiplos = 0
    while cont < 50:
        if cont % numero1 == 0 and cont % numero2 == 0:
           totalMultiplos += 1
        cont += 1
    return totalMultiplos 

numero1 = int(input()) 
numero2 = int(input())

print(ehMultiplos(numero1, numero2)) 

