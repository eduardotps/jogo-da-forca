import random
palavras = ["algoritmico", "raciocicio", "mouse", "programar", "python", "ruby", "surf", "aprovado","array", "vetor", "teclado", "poneis", "malditos", "pneumoultramicroscopicossilicovulcanoconiótico", "Anticonstitucionalissimamente", "Oftalmotorrinolaringologista"]
palavra_sorteada = random.choice(palavras)
palavra_escondida = ["_"] * len(palavra_sorteada)
tentativas = 6

print()
print("----- Jogo da Forca -----")
print()
print("A palavra a ser adivinhada tem", len(palavra_sorteada), "letras.")
print("Você tem", tentativas, "tentativas para adivinhar a palavra.")
print()

escolhas = []
while tentativas > 0 and "_" in palavra_escondida:
    print(" ".join(palavra_escondida))
    print()
    chute = input("Insira uma letra: ")
    print()

    if chute in escolhas:
        print('Letra "', chute, '" já usada! Tente novamente.')
    else:
        if chute in palavra_sorteada:
            for index, letra in enumerate(palavra_sorteada):
                if chute == letra:
                    palavra_escondida[index] = letra
        else:
            tentativas -= 1
            if tentativas == 1:
                print("Errado! Cuidado!!!! Última tentativa!!!")
            elif tentativas == 0:
                print('Errrroooou')
                print()
            else:
                print("Errado! Você tem", tentativas, "tentativas restantes.")
                print()
    escolhas.append(chute)


if palavra_escondida.count('_') == 0:
    print("Você adivinhou a palavra:", ''.join(palavra_escondida), ', parabuains!')
else:
    print("GAME OVER: Você não tem mais tentativas (vacilão!) A palavra secreta era (fácil):", palavra_sorteada.upper())
