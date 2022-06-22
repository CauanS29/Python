força = int(input())
Inteligencia = int(input())
destreza = int(input())
furtividade = int(input())
peso = int(input())

if força > 5 and destreza > 5 and peso > 5:
    print('Knight')
elif força < 5 and Inteligencia > 5 and furtividade > 5 and peso < 5:
    print('Mage')
elif força > 5 and Inteligencia > 5 and destreza > 5 and furtividade > 5 and peso < 5:
    print('Paladin')
elif força > 10 and Inteligencia < 5 and destreza < 5 and furtividade < 5 and peso > 5:
    print ('Orc')
