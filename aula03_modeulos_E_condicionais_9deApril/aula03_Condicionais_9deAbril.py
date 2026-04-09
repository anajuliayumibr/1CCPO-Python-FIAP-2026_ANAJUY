#estrutura simples  (if)
nota_final = 3

if nota_final <6:
    print("Reprovado")

print("FIM")

#composta  (if + else)
nota_final = 5.0

if nota_final <6:
    print("Reprovado")
else:
    print("Aprovado")

print("FIM")

#condicional encadeada (elif)
nota_final = 7.0

if nota_final <4:
    print("Reprovado")

elif nota_final < 6:
        print("Recuperação")
else:
        print("Aprovado")
print("FIM")
