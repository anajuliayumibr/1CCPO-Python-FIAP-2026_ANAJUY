qtd_musicas = int(input("Quantidades de músicas vc tem na playlist? (db): "))

for i in range(qtd_musicas):
    print(f"Músicas {i}")

#laços aninhados
#rep encadeada
for i in range(0, 4):
    for j in range(0, 3, 2):
        print(f"i:{i},  j:{i}")