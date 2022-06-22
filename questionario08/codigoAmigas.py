def decifrarCodigo(posicao) :

    cont  = 0

    for i in " abcdefghijklmnopqrstuvwxyz" : 
          
          if cont == posicao : 
             return i 

          cont += 1

while 3 > 1 : 
      codigo = input().split()
      
      mensagem = ""

      for i in (codigo) : 
          mensagem += decifrarCodigo(int(i)) 

      if mensagem == "fim" :  
         break
      
      else : 
          print(mensagem) 