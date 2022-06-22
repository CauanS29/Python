
todosValores = input().split() 

nota1 = float(todosValores[0]) 
nota2 = float(todosValores[1]) 
nota3 = float(todosValores[2]) 
nota4 = float(todosValores[3])  

media = (nota1 * 1 + nota2 * 2 + nota3 * 3 + nota4 * 4)/10


def AnalisarSituacao (primeiraNota, segundaNota, terceiraNota, quartaNota) : 
    if media >= 9 : 
       return ("aprovado com louvor") 

    elif media >= 7 : 
       return ("aprovado")  

    elif media >= 3 and media < 7 : 
         return("prova final")  

    elif media < 3 : 
        return("reprovado") 

    
print(AnalisarSituacao(nota1, nota2, nota3, nota4))