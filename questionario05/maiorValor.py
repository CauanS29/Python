todosValores = input().split() 

valor1 = int(todosValores[0]) 
valor2 = int(todosValores[1]) 
valor3 = int(todosValores[2])  

def MaiorAB (a, b) :
  return  int((a + b + abs(a - b))/2) 


primeiro_segundo = MaiorAB(valor1, valor2)

maior = MaiorAB(primeiro_segundo, valor3)

print(maior, "eh o maior")