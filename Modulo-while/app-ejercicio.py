    # total de hombres y mujeres por hobby
    # hobby con mas mujeres
	# hobby con menos hombres
	# promedio de peso de los de natacion
	# promedio de estatura de futbol
	# hobby con mas personas
entrada = int(input('Desea Ingresar un Estudiante: (1 Si, 2 No)'))

while entrada == 1:

    nombre = input('Ingrese nombre: ')
    peso = int(input('Ingrese peso: '))
    estatura = int(input('Ingrese estatura: '))
    edad = int(input('Ingrese edad: '))
    sexo = int(input('Tipo sexo 1 Mujer, 2 Hombre: '))

    if sexo == 1:
        hobby = (int(input('¿Cual es tu Hobby? 1: baile, 2: futbol, 3: canto, 4: piano, 5: natacion \n')))
        if hobby == 1:
            baile=+1
        elif hobby == 2:
            futbol=+1
        elif hobby == 3:
            canto=+1
        elif hobby == 4:
            piano=+1
        elif hobby == 5:
            natacion=+1
        else:
            print('Error al ingresar hobby')

    elif sexo == 2:
        hobby = (int(input('¿Cual es tu Hobby? 1: baile, 2: futbol, 3: canto, 4: piano, 5: natacion \n' )))
        if hobby == 1:
            baile=+1
        elif hobby == 2:
            futbol=+1
        elif hobby == 3:
            canto=+1
        elif hobby == 4:
            piano=+1
        elif hobby == 5:
            natacion=+1
        else:
            print('Error al ingresar hobby')
    else:
        print('Error al ingresar sexo')

    entrada = input('Desea Ingresar un Estudiante: (1 Si, 2 No)')

print('# ', baile)
print('# ', futbol)
print('# ', canto)
print('# ', piano)
print('# ', natacion)

    

