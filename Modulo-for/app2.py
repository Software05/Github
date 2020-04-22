palabraSinVocal="\n"
# Indicar al usuario que ingrese una palabra
userWord =  input('Ingrese una palabra: ')
# y asignarlo a la variable userWord.
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
print(palabraSinVocal)