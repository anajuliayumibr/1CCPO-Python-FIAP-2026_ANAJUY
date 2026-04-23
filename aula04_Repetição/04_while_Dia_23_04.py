#while CRESCENTE
cp = 0
while cp <= 3:
    print(f"Produto {cp}")
    cp += 1

#while decrescente de 4 até 1 (incluir) DECRESCENTE
i = 4
while i > 0:
    print(i)
    i -= 1

#Repetição com entrada de usuario
jogar = "SIM"

while jogar.lower() == "sim":
    print("Repete ou inicia o jogo")
    jogar = input("Deseja jogar novamente?")

#continue eh igual um filtro ---- usado para filtrar algo para nao exibir -- Modificador
i = 0
while i < 10:
    i += 1

    if i == 3 or i == 5:
        continue

    print(f"produto {i}")

#Break -- finaliza a estrutura de repetição -- sai do fluxo
i = 0
while i < 10:
    i += 1

    if i == 3 or i == 5:
        continue

    if i == 7:
            break

    print(f"produto {i}")