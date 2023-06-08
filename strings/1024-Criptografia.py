indexLoop = 0
quantidadePalavras = int(input())

while indexLoop < quantidadePalavras:
    fraseInput = input()
    fraseCriptografada = ""

    for i in fraseInput:
        novoCaractere = chr(ord(i) + 3)
        fraseCriptografada += novoCaractere

    fraseCriptografada = fraseCriptografada[::-1]

    for i in fraseCriptografada:
        if fraseCriptografada.index(i) >= len(fraseCriptografada) // 2:
            novoCaractere = chr(ord(i) - 1)
            fraseCriptografada[fraseCriptografada.index(i)] = novoCaractere
    indexLoop += 1
    print(fraseCriptografada)
