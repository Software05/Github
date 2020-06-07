import numpy as np
from tkinter import *
import sys


#Logica
def determinante():
    s = np.array([[int(vx.get()), int(vy.get()), int(vz.get())], [int(x1.get()), int(y1.get()), int(z1.get())], [int(x2.get()), int(y2.get()), int(z2.get())]])
    detS = np.linalg.det(s)
    var.set(round(detS))    #Determinante de S

    x = np.array([[int(vt.get()), int(vy.get()), int(vz.get())], [int(t1.get()), int(y1.get()), int(z1.get())], [int(t2.get()), int(y2.get()), int(z2.get())]])
    detX = np.linalg.det(x)
    varx.set(round(detX))   #Determinante de X

    y = np.array([[int(vx.get()), int(vt.get()), int(vz.get())], [int(x1.get()), int(t1.get()), int(z1.get())], [int(x2.get()), int(t2.get()), int(z2.get())]])
    detY = np.linalg.det(y)
    vary.set(round(detY))   #Determinante de Y

    z = np.array([[int(vx.get()), int(vy.get()), int(vt.get())], [int(x1.get()), int(y1.get()), int(t1.get())], [int(x2.get()), int(y2.get()), int(t2.get())]])
    detZ = np.linalg.det(z)
    varz.set(round(detZ))   #Determinante de Z

    rx = detX/detS
    vrx.set(round(rx)) #Resultado de X

    ry = detY/detS
    vry.set(round(ry)) #Resultado de Y

    rz = detZ/detS
    vrz.set(round(rz)) #Resultado de Z

def delete_ent():
    vx.delete(first=0, last=22)
    vy.delete(first=0, last=22)
    vz.delete(first=0, last=22)
    vt.delete(first=0, last=22)
    x1.delete(first=0, last=22)
    y1.delete(first=0, last=22)
    z1.delete(first=0, last=22)
    t1.delete(first=0, last=22)
    x2.delete(first=0, last=22)
    y2.delete(first=0, last=22)
    z2.delete(first=0, last=22)
    t2.delete(first=0, last=22)

    rs.delete(first=0, last=22)
    rx.delete(first=0, last=22)
    ry.delete(first=0, last=22)
    rz.delete(first=0, last=22)

    rex.delete(first=0, last=22)
    dety.delete(first=0, last=22)
    detz.delete(first=0, last=22)

#-----------------------------------------------------------------------------------

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
img1 = PhotoImage(file="letras/x.png")
lx = Label(root, image=img1).grid(pady=3, row=0, column=0)
vx = Entry(root, width=3, font=50)
vx.grid(row=0, column=1)

img2 = PhotoImage(file="letras/y.png")
ly = Label(root, image=img2).grid(pady=3, row=0, column=2)
vy = Entry(root, width=3, font=50)
vy.grid(row=0, column=3)

img3 = PhotoImage(file="letras/z.png")
lz = Label(root, image=img3).grid(pady=3, row=0, column=4)
vz = Entry(root, width=3, font=50)
vz.grid(row=0, column=5)

img4 = PhotoImage(file="letras/t.png")
lt = Label(root, image=img4).grid(pady=3, row=0, column=6)
vt = Entry(root, width=3, font=50)
vt.grid(row=0, column=7)

#Ecuacion 2
img5 = PhotoImage(file="letras/x.png")
lx1 = Label(root, image=img5).grid(pady=3, row=1, column=0)
x1 = Entry(root, width=3, font=50)
x1.grid(row=1, column=1)

img6 = PhotoImage(file="letras/y.png")
ly1 = Label(root, image=img6).grid(pady=3, row=1, column=2)
y1 = Entry(root, width=3, font=50)
y1.grid(row=1, column=3)

img7 = PhotoImage(file="letras/z.png")
lz1 = Label(root, image=img7).grid(pady=3, row=1, column=4)
z1 = Entry(root, width=3, font=50)
z1.grid(row=1, column=5)

img8 = PhotoImage(file="letras/t.png")
lt1 = Label(root, image=img8).grid(pady=3, row=1, column=6)
t1 = Entry(root,width=3, font=50)
t1.grid(row=1, column=7)

#Ecuacion 3
img9 = PhotoImage(file="letras/x.png")
lx2 = Label(root, image=img9).grid(pady=3, row=2, column=0)
x2 = Entry(root, width=3, font=50)
x2.grid(row=2, column=1)

img10 = PhotoImage(file="letras/y.png")
ly2 = Label(root, image=img10).grid(pady=3, row=2, column=2)
y2 = Entry(root, width=3, font=50)
y2.grid(row=2, column=3)

img11 = PhotoImage(file="letras/z.png")
lz2 = Label(root, image=img11).grid(pady=3, row=2, column=4)
z2 = Entry(root, width=3, font=50)
z2.grid(row=2, column=5)

img12 = PhotoImage(file="letras/t.png")
lt2 = Label(root, image=img12).grid(pady=3, row=2, column=6)
t2 = Entry(root, width=3, font=50)
t2.grid(row=2, column=7)


#Resultados
cs = PhotoImage(file="icon.png")
lrs = Label(root, image=cs).grid(pady=3, row=0, column=10)
x=Label(root, text='S').grid(row=0, column=11)
rs = Entry(root, textvariable=var, width=7, font=50, state=DISABLED).grid(padx=5, row=0, column=12)

cs1 = PhotoImage(file="icon.png")
lrx = Label(root, image=cs1).grid(pady=3, row=1, column=10)
x=Label(root, text='X').grid(row=1, column=11)
rx = Entry(root, textvariable=varx, width=7, font=50, state=DISABLED).grid(padx=5, row=1, column=12)

cs2 = PhotoImage(file="icon.png")
lry = Label(root, image=cs2).grid(pady=3, row=2, column=10)
x=Label(root, text='Y').grid(row=2, column=11)
ry = Entry(root, textvariable=vary, width=7, font=50, state=DISABLED).grid(padx=5, row=2, column=12)

cs3 = PhotoImage(file="icon.png")
lrz = Label(root, image=cs3).grid(pady=3, row=3, column=10)
x=Label(root, text='Z').grid(row=3, column=11)
rz = Entry(root, textvariable=varz, width=7, font=50, state=DISABLED).grid(padx=5, row=3, column=12)

# X Y Z
cal = Button(root, text="X =", command=determinante).grid(pady=3, row=0, column=13)
rex = Entry(root, textvariable=vrx, width=7, font=50, state=DISABLED).grid(padx=5, row=0, column=14)

cal = Button(root, text="Y =", command=determinante).grid(pady=3, row=1, column=13)
dety = Entry(root, textvariable=vry, width=7, font=50, state=DISABLED).grid(padx=5, row=1, column=14)

cal = Button(root, text="Z =", command=determinante).grid(pady=3, row=2, column=13)
detz = Entry(root, textvariable=vrz, width=7, font=50, state=DISABLED).grid(padx=5, row=2, column=14)

#Borrar Datos
delete = Button(root, text='Limpiar', command=delete_ent).grid(row=3, column=15)
#Boton calcular
calcular = Button(root, text="Calcular", command=determinante).grid(pady=3, row=3, column=13)

root.mainloop()