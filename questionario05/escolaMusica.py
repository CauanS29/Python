mediaAluno = float(input()) 
faltasAluno = int(input()) 

def ClassificaAluno (media, faltas) : 
    if media >= 7 and media < 9.5 and faltas <= 10 : 
       return ("APROVADO") 
    
    elif media >= 9.5 and faltas <= 10 : 
        return ("APROVADO COM LOUVOR") 

    elif media >= 7 and faltas > 10 : 
         return ("REPROVADO POR FALTAS") 

    elif media < 7 : 
        return ("REPROVADO") 




print( ClassificaAluno(mediaAluno, faltasAluno) )

    