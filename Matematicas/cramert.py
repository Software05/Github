from tkinter import *
import numpy as np

def determinanteS():
    s = np.array([[int(capx.get()), int(capy.get()), int(capz.get())], [int(capxu.get()), int(capyu.get()), int(capzu.get())], [int(capxd.get()), int(capyd.get()), int(capzd.get())]])
    determinanteS = np.linalg.det(s)
    return var.set(round(determinanteS))

root = Tk()
root.title('Regla Cramer')

var=StringVar()

#Primera ecuacion
labelx = Label(root, text = 'X =', width=10).grid(pady=3, row=0, column=0)
capx = Entry(root, width=5).grid(padx=5, row=0, column=1)

labely = Label(root, text = 'Y =', width=10).grid(pady=5, row=0, column=2)
capy = Entry(root, width=5).grid(padx=5, row=0, column=3)

labelz = Label(root, text = 'Z =', width=10).grid(pady=5, row=0, column=4)
capz = Entry(root, width=5).grid(padx=5, row=0, column=5)

labelt = Label(root, text = 'T.I =', width=10).grid(pady=5, row=0, column=6)
capt = Entry(root, width=5).grid(padx=5, row=0, column=7)

#Segunda ecuacion
labelxu = Label(root, text = 'X =', width=10).grid(pady=3, row=1, column=0)
capxu = Entry(root, width=5).grid(padx=5, row=1, column=1)

labelyu = Label(root, text = 'Y =', width=10).grid(pady=5, row=1, column=2)
capyu = Entry(root, width=5).grid(padx=5, row=1, column=3)

labelzu = Label(root, text = 'Z =', width=10).grid(pady=5, row=1, column=4)
capzu = Entry(root, width=5).grid(padx=5, row=1, column=5)

labeltu = Label(root, text = 'T.I =', width=10).grid(pady=5, row=1, column=6)
captu = Entry(root, width=5).grid(padx=5, row=1, column=7)

#Tercera ecuacion
labelxd = Label(root, text = 'X =', width=10).grid(pady=3, row=2, column=0)
capxd = Entry(root, width=5).grid(padx=5, row=2, column=1)

labelyd = Label(root, text = 'Y =', width=10).grid(pady=5, row=2, column=2)
capyd = Entry(root, width=5).grid(padx=5, row=2, column=3)

labelzd = Label(root, text = 'Z =', width=10).grid(pady=5, row=2, column=4)
capzd = Entry(root, width=5).grid(padx=5, row=2, column=5)

labeltd = Label(root, text = 'T.I =', width=10).grid(pady=5, row=2, column=6)
captd = Entry(root, width=5).grid(padx=5, row=2, column=7)

#Botones
calcular = Button(root, text='Calcular', command=determinanteS).grid(row=4, column=3)

#Resultados

labelrex = Label(root, text = 'DET S', width=0).grid(pady=0, row=3, column=0)
rex = Entry(root, textvariable=var, width=5).grid(padx=5, row=3, column=1)

labelrex = Label(root, textvariable=var, width=0).grid(pady=0, row=5, column=1)

root.mainloop()