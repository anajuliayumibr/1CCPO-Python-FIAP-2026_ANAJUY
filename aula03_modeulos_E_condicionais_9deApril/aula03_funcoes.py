#criar funcoes

#funcao SEM retorno e sem parametro
def print_lyrics():
    print("I ain't gonna live forever")                          #Ajustar Identacao eh Ctrl + Tab
    print("I just want to live while I'm alive")

print_lyrics()
print_lyrics()


#Funcao sem retorno e com parametro
def boas_vindas(nome):
    print(f"Olá, {nome}!!! Seja Bem-vindo.")

nome_digitado = input("Digite seu nome: ")
boas_vindas(nome_digitado)

#Funcao com retorno e com parametro
def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

resultado_soma = soma(17, 22)
print(resultado_soma)



