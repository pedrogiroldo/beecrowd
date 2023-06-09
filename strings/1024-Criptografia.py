indexLoop = 0
quantidadePalavras = int(input())

while indexLoop < quantidadePalavras:
    fraseInput = input()
    novaFraseCriptografada = ""
    fraseCriptografada = ""

    for i in fraseInput:
        novoCaractere = chr(ord(i) + 3)
        fraseCriptografada += novoCaractere

    fraseCriptografada = fraseCriptografada[::-1]

    for i in range(len(fraseCriptografada)):
        if i >= len(fraseCriptografada) // 2:
            novoCaractere = chr(ord(fraseCriptografada[i]) - 1)
            novaFraseCriptografada += novoCaractere
        else:
            novaFraseCriptografada += fraseCriptografada[i]
    fraseCriptografada = novaFraseCriptografada
    print(fraseCriptografada)
    indexLoop += 1
