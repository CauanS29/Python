from posixpath import split


def formato(email): 

    situacaoEmail = "certo" 

    if email.count(".") != 2 : 

       situacaoEmail = "errado" 

    elif email[0] == "@" : 
        
       situacaoEmail = "errado" 

    
    elif email.index("@") + 1 == email.index(".") : 

        situacaoEmail = "errado"

    email = email.split(".") 

    if email[0] == "." : 

        situacaoEmail = "errado" 

    elif len(email) < 3 : 

        situacaoEmail = "errado" 

    elif (email[0] == "") or (email[1] == "") or (email[2] ==  "") : 
        
        situacaoEmail = "errado" 

    return situacaoEmail


while True : 

    email = input() 

    if email == "sair" : 
        break 

    print(formato(email))