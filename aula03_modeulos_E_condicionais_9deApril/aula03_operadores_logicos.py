#dentro do if pode deixar muito mais complexo
#Logica E (and) ex= email e senha

verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha   #tem o OR também, mas para Login nao faz sentido
print(login)

if login:
    print("Entra no sistema")

#Logica inversa
verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha  
print(login)

if not login:
    print("loga certo ai cara!")