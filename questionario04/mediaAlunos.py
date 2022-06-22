nota1 = float(input()) 
nota2 = float(input()) 
nota3 = float(input()) 

situacaoAluno = "aprovado" 

mediaAluno = (nota1 + nota2 + nota3)/3

if mediaAluno < 3 : 
   situacaoAluno = "reprovado" 

elif mediaAluno >= 3 and mediaAluno < 7 : 
     situacaoAluno = "prova final"  

print(situacaoAluno) 