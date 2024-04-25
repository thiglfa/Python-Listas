sorteada = "frango assado"
erros = 0
chutadas = " "

segredo = ""
for c in sorteada:
    if c in chutadas:
        segredo = segredo + c + " "
    else:
        segredo = segredo + "_ "

while erros < 6 and "_" in segredo:
    print(f"{segredo}\nerros: {erros}")
    letra = input("Informe a letra: ").lower()
    chutadas = chutadas + letra
    print(chutadas)

    segredo = ""
    for c in sorteada:
        if c in chutadas:
            segredo = segredo + c + " "
        else:
            segredo = segredo + "_ "
    if not letra in sorteada:
        erros = erros + 1
if erros == 6:
    print(f"Você errou {erros} vezes e a palavra era {sorteada}")
else:
    print(f"Parabéns, você acertou {sorteada}")

#pegue a letra digitada e gere o novo segredo
#suponha que a letra informada seja o a
#segredo -> _ _ a _ _    a _ _ a _ _