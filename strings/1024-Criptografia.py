fraseInput = input()
fraseCriptografada = ''

for i in fraseInput:
    novoCaractere = chr(ord(i) + 3)
    fraseCriptografada += novoCaractere

fraseCriptografada = fraseCriptografada[::-1]

print(fraseCriptografada)