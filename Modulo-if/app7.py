anio = int(input('Introduzca un año: '))

if anio%4 != 0:
    print('Año común')
elif anio <= 1582:
    print('No dentro del período del calendario gregoriano')
else:
    print('Año Bisiesto')