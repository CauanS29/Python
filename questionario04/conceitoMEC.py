quantidadeLivros = int(input()) 
quantidadeAlunos = int(input()) 

contaMedia = quantidadeAlunos/quantidadeLivros 

conceito = "B" 

if contaMedia <= 8 : 
   conceito = "A" 

elif contaMedia >= 13 and contaMedia <= 18 : 
     conceito = "C" 

elif contaMedia > 18 : 
     conceito = "D"  

print(conceito) 