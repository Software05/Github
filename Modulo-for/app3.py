palabraSinVocal = ""

# Indicar al usuario que ingrese una palabra
userWord = input('Ingrese la palabra: ')
# y asignarlo a la variable userWord
userWord = userWord.upper()


for letra in userWord:
    if letra == 'A':
        continue
    if letra == 'E':
        continue
    if letra == 'I':
        continue
    if letra == 'O':
        continue
    if letra == 'U':
        continue
    print(letra, end='')

# Imprimir la palabra asignada a palabraSinVocal.
print(palabraSinVocal)
