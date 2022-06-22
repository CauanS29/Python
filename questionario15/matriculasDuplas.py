listaAlunos = input().split() 

listaAlunos2 = input().split() 

listaDuplicados = []


for alunos in listaAlunos : 

    if alunos in listaAlunos2:  
        listaDuplicados.append(alunos)  

texto =" ".join(listaDuplicados) 

print(texto)



