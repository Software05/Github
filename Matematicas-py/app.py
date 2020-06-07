import numpy as np
from tkinter import *
import sys

#Logica
def determinanteS():
    s = np.array([[int(vx.get()), int(vy.get()), int(vz.get())], [int(x1.get()), int(y1.get()), int(z1.get())], [int(x2.get()), int(y2.get()), int(z2.get())]])
    detS = np.linalg.det(s)
    var.set(round(detS))

def determinanteX():
    x = np.array([[int(vt.get()), int(vy.get()), int(vz.get())], [int(t1.get()), int(y1.get()), int(z1.get())], [int(t2.get()), int(y2.get()), int(z2.get())]])
    detX = np.linalg.det(x)
    varx.set(round(detX))

def determinanteY():
    y = np.array([[int(vx.get()), int(vt.get()), int(vz.get())], [int(x1.get()), int(t1.get()), int(z1.get())], [int(x2.get()), int(t2.get()), int(z2.get())]])
    detY = np.linalg.det(y)
    vary.set(round(detY))

def determinanteZ():
    z = np.array([[int(vx.get()), int(vy.get()), int(vt.get())], [int(x1.get()), int(y1.get()), int(t1.get())], [int(x2.get()), int(y2.get()), int(t2.get())]])
    detZ = np.linalg.det(z)
    varz.set(round(detZ))

def resultx():
    rex = detX/detS
    vrx.set(round(rex))

root = Tk()
root.title('Regla Cramer')

var = IntVar()  #Determinante de S
varx = IntVar() #Determinante de X
vrx = IntVar()  #Resultado de X
vary = IntVar() #Determinante de Y
vry = IntVar()  #Resultado de Y
varz = IntVar() #Determinante de Z
vrz = IntVar()  #Resultado de Z

#Ecuacion 1
lx = Label(root, text='X =', width=2).grid(pady=3, row=0, column=0)
vx = Entry(root, width=5)
vx.grid(padx=5, row=0, column=1)

ly = Label(root, text='Y =', width=2).grid(pady=3, row=0, column=2)
vy = Entry(root, width=5)
vy.grid(padx=5, row=0, column=3)

lz = Label(root, text='Z =', width=2).grid(pady=3, row=0, column=4)
vz = Entry(root, width=5)
vz.grid(padx=5, row=0, column=5)

lt = Label(root, text='T.I =', width=2).grid(pady=3, row=0, column=6)
vt = Entry(root, width=5)
vt.grid(padx=5, row=0, column=7)

#Ecuacion 2
lx1 = Label(root, text='X =', width=2).grid(pady=3, row=1, column=0)
x1 = Entry(root, width=5)
x1.grid(padx=5, row=1, column=1)

ly1 = Label(root, text='Y =', width=2).grid(pady=3, row=1, column=2)
y1 = Entry(root, width=5)
y1.grid(padx=5, row=1, column=3)

lz1 = Label(root, text='Z =', width=2).grid(pady=3, row=1, column=4)
z1 = Entry(root, width=5)
z1.grid(padx=5, row=1, column=5)

lt1 = Label(root, text='T.I =', width=2).grid(pady=3, row=1, column=6)
t1 = Entry(root, width=5)
t1.grid(padx=5, row=1, column=7)

#Ecuacion 3
lx2 = Label(root, text='X =', width=2).grid(pady=3, row=2, column=0)
x2 = Entry(root, width=5)
x2.grid(padx=5, row=2, column=1)

ly2 = Label(root, text='Y =', width=2).grid(pady=3, row=2, column=2)
y2 = Entry(root, width=5)
y2.grid(padx=5, row=2, column=3)

lz2 = Label(root, text='Z =', width=2).grid(pady=3, row=2, column=4)
z2 = Entry(root, width=5)
z2.grid(padx=5, row=2, column=5)

lt2 = Label(root, text='T.I =', width=2).grid(pady=3, row=2, column=6)
t2 = Entry(root, width=5)
t2.grid(padx=5, row=2, column=7)

#Botones
calcular = Button(root, text="S =", command=determinanteS).grid(pady=3, row=0, column=9)
calcular = Button(root, text="X =", command=determinanteX).grid(pady=3, row=1, column=9)
calcular = Button(root, text="Y =", command=determinanteY).grid(pady=3, row=2, column=9)
calcular = Button(root, text="Z =", command=determinanteZ).grid(pady=3, row=3, column=9)

#Resultados
lrs = Label(root, text='DT S =', width=2).grid(pady=3, row=0, column=10)
rs = Entry(root, textvariable=var, width=5).grid(padx=5, row=0, column=11)

lrx = Label(root, text='DT X =', width=2).grid(pady=3, row=1, column=10)
rx = Entry(root, textvariable=varx, width=5).grid(padx=5, row=1, column=11)

lry = Label(root, text='DT Y =', width=2).grid(pady=3, row=2, column=10)
ry = Entry(root, textvariable=vary, width=5).grid(padx=5, row=2, column=11)

lrz = Label(root, text='DT Z =', width=2).grid(pady=3, row=3, column=10)
rz = Entry(root, textvariable=varz, width=5).grid(padx=5, row=3, column=11)


# X Y Z
cal = Button(root, text="X =", command=resultx).grid(pady=3, row=0, column=12)
rex = Entry(root, textvariable=vrx, width=5).grid(padx=5, row=0, column=14)

cal = Button(root, text="Y =", command=determinanteS).grid(pady=3, row=1, column=12)
dety = Entry(root, textvariable=vrz, width=5).grid(padx=5, row=1, column=14)

cal = Button(root, text="Z =", command=determinanteS).grid(pady=3, row=2, column=12)
detz = Entry(root, textvariable=vrz, width=5).grid(padx=5, row=2, column=14)



root.mainloop()