numero1 = int(input())  
numero2 = int(input()) 
operacao = input() 


def resultadoOperacao(numero1, numero2, operacao) :  
    resultado = numero1 + numero2
    
    if operacao == "-" : 
      resultado = numero1 - numero2 
      
    elif operacao == "*" : 
      resultado = numero1 * numero2 

    elif operacao == "/" : 
      resultado = numero1 / numero2 

    return resultado
    

calculo = resultadoOperacao(numero1, numero2, operacao)
print("%.3f"%calculo) 

while True : 
      novoNumero = float(input()) 
      novaOperacao = input() 

      if novaOperacao == "&" : 
          break 

      if novoNumero == 0  and novaOperacao == "/" : 
         print("operacao nao pode ser realizada") 
         continue 

      resultado = resultadoOperacao(calculo, novoNumero, novaOperacao) 
      print("%.3f"%resultado) 

      calculo = resultado 