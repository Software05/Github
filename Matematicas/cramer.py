import numpy as np

#Datos primer ecuación
numx = float(input('x: '))
numy = float(input('y: '))
numz = float(input('z: '))
numt = float(input('t: '))

#Datos segunda ecuación
numxu = float(input('x1: '))
numyu = float(input('y1: '))
numzu = float(input('z1: '))
numtu = float(input('t1: '))

#Datos tercera ecuación
numxd = float(input('x2: '))
numyd = float(input('y2: '))
numzd = float(input('z2: '))
numtd = float(input('t2: '))

#Matriz del Sistema
s = np.array([[numx, numy, numz], [numxu, numyu, numzu], [numxd, numyd, numzd]])
print('Matriz s')
print(s)

#Matriz de X
x = np.array([[numt, numy, numz], [numtu, numyu, numzu], [numtd, numyd, numzd]])
print('Matriz x')
print(x)

#Matriz de Y
y = np.array([[numx, numt, numz], [numxu, numtu, numzu], [numxd, numtd, numzd]])
print('Matriz y')
print(y)

#Matriz de Z
z = np.array([[numx, numy, numt], [numxu, numyu, numtu], [numxd, numyd, numtd]])
print('Matriz z')
print(z)


determinanteS = np.linalg.det(s)
determinanteX = np.linalg.det(x)
determinanteY = np.linalg.det(y)
determinanteZ = np.linalg.det(z)

print('Determinante Sistema', round(determinanteS))
print('Determinante X', round(determinanteX))
print('Determinante Y', round(determinanteY))
print('Determinante Z', round(determinanteZ))

rx = determinanteX/determinanteS
ry = determinanteY/determinanteS
rz = determinanteZ/determinanteS

print('X =', rx)
print('y =', ry)
print('z =', rz)

# 1 1 1 37      
# -1 -1 3 3       
# -1 1 -1 -13