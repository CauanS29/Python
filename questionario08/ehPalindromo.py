def ehPalindromo(palavra1): 

    return palavra1 == palavra1[::-1] 

numeroPalindromos = int(input()) 

def ehEspaco(palavra1): 

    restoPalavra = ""

    for i in palavra1 : 

        if i != " " : 
           restoPalavra += i 

    return restoPalavra


for i in range(0, numeroPalindromos): 
    palavra1 = ehEspaco(input().lower()) 
    
    resultado = "NAO"

    if ehPalindromo(palavra1) : 
       resultado = "SIM" 
    
    print(resultado) 






    
